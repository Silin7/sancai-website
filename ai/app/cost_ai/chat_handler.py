# app/cost_ai/chat_handler.py
# 造价AI聊天API处理器
import asyncio
from flask import Blueprint, request, jsonify, render_template, session
from app.data_storage.user_manager import init_user_session
from .query_generator import generate_sql, format_response, analyze_intent, generate_sql_for_table
from . import db_service
from . import conversation_storage as storage

cost_ai_bp = Blueprint('cost_ai', __name__)

# ==================== 辅助函数 ====================

# 无法生成SQL时的关键词检测列表
# 当description包含这些关键词时，说明AI无法理解问题或需要用户提供更多信息
UNABLE_TO_GENERATE_KEYWORDS = [
    '例如', '比如您可以', '可以尝试', '您可能想'
]

def _get_version_info(user_id, conv_id, pair_id):
    """获取当前消息的版本统计信息"""
    if not (user_id and conv_id and pair_id):
        return 1, 0
    try:
        from . import conversation_storage as storage
        conv_data = storage.get_conversation(user_id, conv_id)
        for m in conv_data.get('messages', []):
            if m['role'] == 'assistant' and m.get('pair_id') == pair_id:
                versions = m.get('versions', [m['content']])
                return len(versions), m.get('active_index', 0)
    except:
        pass
    return 1, 0

def _is_unable_to_generate_sql(sql_info):
    """
    判断AI是否无法生成有效的SQL查询
    
    Args:
        sql_info: generate_sql返回的结果字典
        
    Returns:
        tuple: (is_unable: bool, response_text: str)
            - is_unable: True表示无法生成有效SQL，需要直接返回response_text
            - response_text: 要返回给用户的文本
    """
    if not sql_info:
        return True, '抱歉，处理请求时出错，请稍后重试。'
    
    # 检查sql是否为None或空
    if not sql_info.get('sql'):
        description = sql_info.get('description', '')
        if description:
            return True, description
        return True, '抱歉，我无法理解您的问题，请尝试换一种方式提问。'
    
    # 检查description是否包含"无法生成"类关键词
    # 有时AI虽然返回了sql，但description中包含提示性文字，说明SQL可能不准确
    description = sql_info.get('description', '')
    for keyword in UNABLE_TO_GENERATE_KEYWORDS:
        if keyword in description:
            return True, description
    
    return False, None

def _save_assistant_response(user_id, conv_id, pair_id, content, regenerate_pair_id=None):
    """
    统一保存AI助手回复逻辑
    """
    if not (user_id and conv_id and content):
        return None
        
    if regenerate_pair_id:
        # 检查是否已有该 pair_id 的助手消息
        conv_data = storage.get_conversation(user_id, conv_id)
        exists = False
        for m in conv_data.get('messages', []):
            if m['role'] == 'assistant' and m.get('pair_id') == pair_id:
                exists = True
                break
        
        if exists:
            return storage.add_message_version(user_id, conv_id, pair_id, content)
        else:
            # 重试场景：虽然是重新生成，但之前没有AI回复，所以新建一条并指定 pair_id
            return storage.add_message(user_id, conv_id, 'assistant', content, pair_id=pair_id)
    else:
        # 正常新消息
        return storage.add_message(user_id, conv_id, 'assistant', content)

async def _execute_multi_table_query(question: str, tables: list) -> tuple:
    """
    对多个表执行查询并合并结果
    
    Args:
        question: 用户问题
        tables: 要查询的表名列表
        
    Returns:
        tuple: (all_results, errors) - all_results是合并后的结果列表
    """
    all_results = []
    errors = []
    
    for table_name in tables:
        # 为每个表生成SQL
        sql, sql_error = generate_sql_for_table(question, table_name)
        
        if sql_error:
            errors.append(f"{table_name}: {sql_error}")
            continue
        
        print(f"【多表查询】表 {table_name}: {sql}")
        
        # 执行查询
        results, db_error = await db_service.execute_query(sql)
        
        if db_error:
            errors.append(f"{table_name}: {db_error}")
            continue
        
        if results:
            # 为每条结果添加来源表标记
            for r in results:
                r['_source_table'] = table_name
            all_results.extend(results)
    
    return all_results, errors

@cost_ai_bp.route('/cost-ai')
@cost_ai_bp.route('/cost-ai/')
@cost_ai_bp.route('/cost-ai/<conv_id>')
def cost_ai_page(conv_id=None):
    """渲染造价AI页面"""
    init_user_session()
    user_id = session.get('user_id')
    conversations = storage.load_conversations(user_id) if user_id else []
    #return render_template('cost-ai.html', conversations=conversations)
    return render_template('cost-ai-blue2.html', conversations=conversations)

# ==================== 对话历史API ====================

@cost_ai_bp.route('/api/cost-ai/conversations', methods=['GET'])
def get_conversations():
    """获取对话列表"""
    init_user_session()
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'error': '用户未登录'})
    
    conversations = storage.load_conversations(user_id)
    return jsonify({'success': True, 'conversations': conversations})

@cost_ai_bp.route('/api/cost-ai/conversations', methods=['POST'])
def create_conversation():
    """创建新对话"""
    init_user_session()
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'error': '用户未登录'})
    
    conv = storage.create_conversation(user_id)
    return jsonify({'success': True, 'conversation': conv})

@cost_ai_bp.route('/api/cost-ai/conversations/<conv_id>', methods=['GET'])
def get_conversation(conv_id):
    """获取单个对话详情"""
    init_user_session()
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'error': '用户未登录'})
    
    # 剥离前缀（健壮性）
    if conv_id.startswith('conv_'):
        conv_id = conv_id[5:]
    
    conv = storage.get_conversation(user_id, conv_id)
    return jsonify({'success': True, 'messages': conv.get('messages', [])})

@cost_ai_bp.route('/api/cost-ai/conversations/<conv_id>', methods=['DELETE'])
def delete_conversation(conv_id):
    """删除对话"""
    import logging
    logger = logging.getLogger(__name__)
    
    try:
        init_user_session()
        user_id = session.get('user_id')
        if not user_id:
            logger.warning("删除对话失败：用户未登录")
            return jsonify({'success': False, 'error': '用户未登录'}), 401
        
        # 剥离前缀（健壮性）
        if conv_id.startswith('conv_'):
            conv_id = conv_id[5:]
        
        logger.info(f"用户 {user_id} 请求删除对话 {conv_id}")
        
        # 调用删除函数
        success = storage.delete_conversation(user_id, conv_id)
        
        if success:
            logger.info(f"成功删除对话 {conv_id}")
            return jsonify({'success': True, 'message': '对话已删除'})
        else:
            logger.warning(f"删除对话 {conv_id} 返回 False")
            return jsonify({'success': False, 'error': '对话不存在或删除失败'}), 404
            
    except Exception as e:
        logger.error(f"删除对话 {conv_id} 时发生异常: {e}", exc_info=True)
        return jsonify({
            'success': False, 
            'error': '删除对话时发生错误',
            'detail': str(e)
        }), 500

@cost_ai_bp.route('/api/cost-ai/conversations/<conv_id>/title', methods=['PUT'])
def update_conversation_title(conv_id):
    """更新对话标题"""
    init_user_session()
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'error': '用户未登录'})
    
    # 剥离前缀（健壮性）
    if conv_id.startswith('conv_'):
        conv_id = conv_id[5:]
    
    data = request.get_json()
    new_title = data.get('title')
    
    if not new_title:
        return jsonify({'success': False, 'error': '标题不能为空'})
        
    success = storage.update_conversation_title(user_id, conv_id, new_title)
    if success:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': '更新失败，对话不存在'})

@cost_ai_bp.route('/api/cost-ai/conversations/<conv_id>/messages/<int:pair_id>/switch', methods=['POST'])
def switch_version(conv_id, pair_id):
    """切换消息版本"""
    init_user_session()
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'error': '用户未登录'})
    
    # 剥离前缀（健壮性）
    if conv_id.startswith('conv_'):
        conv_id = conv_id[5:]
        
    data = request.get_json()
    version_index = data.get('index')
    
    if version_index is None:
        return jsonify({'success': False, 'error': '未指定版本索引'})
        
    success = storage.switch_message_version(user_id, conv_id, pair_id, version_index)
    if success:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': '切换失败，消息或版本不存在'})

# ==================== 聊天API ====================

@cost_ai_bp.route('/api/cost-ai/chat', methods=['POST'])
def chat():
    """处理聊天请求"""
    import logging
    logger = logging.getLogger(__name__)
    
    init_user_session()
    user_id = session.get('user_id')
    
    # 尝试获取数据（兼容 JSON 和 Multipart/Form-Data）
    if request.is_json:
        data = request.get_json()
    else:
        # 处理 application/x-www-form-urlencoded 或 multipart/form-data
        data = request.form.to_dict()
        
    message = data.get('message', '').strip()
    conv_id = data.get('conversation_id')
    regenerate_pair_id = data.get('regenerate_pair_id')
    
    logger.info(f"========== 新的聊天请求 ==========")
    logger.info(f"用户ID: {user_id}")
    logger.info(f"用户消息: {message}")
    logger.info(f"对话ID: {conv_id}")
    logger.info(f"重新生成对ID: {regenerate_pair_id}")
    
    # Check for files
    files = request.files.getlist('files')
    if files:
        # TODO: Handle file saving logic here if needed for analysis
        pass

    if not message and not files and not regenerate_pair_id:
        return jsonify({'success': False, 'error': '消息不能为空'})
    
    # 如果没有对话ID，创建新对话
    if not conv_id and user_id:
        conv = storage.create_conversation(user_id, message[:20])
        conv_id = conv['id']
    
    # 保存或获取消息
    pair_id = None
    if regenerate_pair_id:
        # 重新生成逻辑
        pair_id = int(regenerate_pair_id)
        # 补丁：更新原消息的时间戳，符合用户“重发”逻辑
        storage.update_message_time(user_id, conv_id, pair_id)
        
        conv_data = storage.get_conversation(user_id, conv_id)
        for m in conv_data.get('messages', []):
            if m['role'] == 'user' and m.get('pair_id') == pair_id:
                message = m['content']
                break
    else:
        # 正常保存用户消息
        if user_id and conv_id:
            msg_obj = storage.add_message(user_id, conv_id, 'user', message)
            pair_id = msg_obj.get('pair_id')
    
    try:
        # 1. 使用AI生成SQL
        logger.info("步骤1: 调用generate_sql生成查询语句...")
        sql_info, error = generate_sql(message)
        
        logger.info(f"generate_sql返回: sql_info={sql_info}, error={error}")
        
        # 检查是否有错误
        if error:
            logger.error(f"生成SQL时出错: {error}")
            response_text = f'抱歉，处理请求时出错: {error}'
            _save_assistant_response(user_id, conv_id, pair_id, response_text, regenerate_pair_id)
            v_count, a_idx = _get_version_info(user_id, conv_id, pair_id)
            return jsonify({
                'success': True,
                'message': response_text,
                'conversation_id': conv_id,
                'versions_count': v_count,
                'active_index': a_idx,
                'data': None
            })
        
        # 检查是否无法生成有效SQL
        is_unable, response_text = _is_unable_to_generate_sql(sql_info)
        if is_unable:
            logger.warning(f"无法生成有效SQL: {response_text}")
            _save_assistant_response(user_id, conv_id, pair_id, response_text, regenerate_pair_id)
            v_count, a_idx = _get_version_info(user_id, conv_id, pair_id)
            return jsonify({
                'success': True,
                'message': response_text,
                'conversation_id': conv_id,
                'versions_count': v_count,
                'active_index': a_idx,
                'data': None
            })
        
        # 2. 执行SQL查询
        sql_query = sql_info['sql']
        logger.info(f"步骤2: 执行SQL查询")
        logger.info(f"SQL语句: {sql_query}")
        logger.info(f"SQL描述: {sql_info.get('description', 'N/A')}")
        
        print("\n" + "#"*50)
        print(f"【数据库查询】")
        print(f"执行 SQL: {sql_query}")
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            results, db_error = loop.run_until_complete(
                db_service.execute_query(sql_query)
            )
        finally:
            loop.close()
        
        print(f"查询结果: 返回 {len(results) if results else 0} 条记录")
        if db_error:
            print(f"数据库错误: {db_error}")
        print("#"*50 + "\n")
        
        logger.info(f"查询结果: 返回 {len(results) if results else 0} 条记录")
        if results:
            logger.info(f"结果样例(前3条): {results[:3]}")
        logger.info(f"数据库错误: {db_error}")
        
        if db_error:
            logger.error(f"数据库查询失败: {db_error}")
            return jsonify({
                'success': False,
                'error': f"数据库查询失败: {db_error}"
            })
        
        # 3. 格式化结果
        logger.info(f"步骤3: 格式化查询结果...")
        
        # 增加 Decimal 处理（转换为 float 或 string）
        from decimal import Decimal
        def _serialize_decimal(obj):
            if isinstance(obj, Decimal):
                return float(obj)
            return obj

        if results:
            processed_results = []
            for r in results:
                processed_row = {k: _serialize_decimal(v) for k, v in r.items()}
                processed_results.append(processed_row)
            results = processed_results

        response_text = format_response(message, results)
        logger.info(f"格式化后的回复: {response_text[:200]}...")  # 只打印前200字符
        
        # 保存AI回复
        _save_assistant_response(user_id, conv_id, pair_id, response_text, regenerate_pair_id)
        
        v_count, a_idx = _get_version_info(user_id, conv_id, pair_id)
        
        logger.info(f"========== 请求处理完成 ==========\n")
        
        return jsonify({
            'success': True,
            'message': response_text,
            'conversation_id': conv_id,
            'versions_count': v_count,
            'active_index': a_idx,
            'data': {
                'sql': sql_info['sql'],
                'table': sql_info.get('table'),
                'count': len(results) if results else 0,
                'pair_id': pair_id
            }
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


# ==================== SSE流式聊天API ====================

@cost_ai_bp.route('/api/cost-ai/chat/stream', methods=['POST'])
def chat_stream():
    """
    SSE流式聊天接口
    
    当 COST_AI_STREAM_ENABLED 开关启用时，返回SSE流式响应。
    响应格式：text/event-stream
    每个chunk格式：data: {"text": "一段文本"}\n\n
    结束标记：data: [DONE]\n\n
    """
    import json
    import logging
    from flask import Response, stream_with_context
    from app.config import Config
    from .stream_ai import stream_ai_response, get_stream_enabled
    
    logger = logging.getLogger(__name__)
    
    init_user_session()
    user_id = session.get('user_id')
    
    # 获取请求数据
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()
    
    message = data.get('message', '').strip()
    conv_id = data.get('conversation_id')
    regenerate_pair_id = data.get('regenerate_pair_id')
    
    logger.info(f"========== 新的流式聊天请求 ==========")
    logger.info(f"用户ID: {user_id}")
    logger.info(f"用户消息: {message}")
    logger.info(f"对话ID: {conv_id}")
    logger.info(f"重新生成对ID: {regenerate_pair_id}")
    
    if not message and not regenerate_pair_id:
        return jsonify({'success': False, 'error': '消息不能为空'}), 400
    
    # 如果没有对话ID，创建新对话
    if not conv_id and user_id:
        conv = storage.create_conversation(user_id, message[:20])
        conv_id = conv['id']
    
    # 计算 pair_id
    pair_id = None
    if regenerate_pair_id:
        pair_id = int(regenerate_pair_id)
        # 补丁：更新原消息的时间戳
        storage.update_message_time(user_id, conv_id, pair_id)
        
        conv_data = storage.get_conversation(user_id, conv_id)
        for m in conv_data.get('messages', []):
            if m['role'] == 'user' and m.get('pair_id') == pair_id:
                message = m['content']
                break
    else:
        # 保存用户消息
        if user_id and conv_id:
            msg_obj = storage.add_message(user_id, conv_id, 'user', message)
            pair_id = msg_obj.get('pair_id')
    
    def generate():
        """SSE响应生成器"""
        full_response = []
        
        def _yield_stream_text(text, is_done=False, v_count=None, a_idx=None):
            """模拟流式推送文本块"""
            # 发送数据基础包
            base_data = {
                'conversation_id': conv_id, 
                'pair_id': pair_id
            }
            if v_count is not None: base_data['versions_count'] = v_count
            if a_idx is not None: base_data['active_index'] = a_idx

            # 如果文本很短，直接发送
            if len(text) <= 5:
                data = base_data.copy()
                data.update({'text': text, 'done': is_done})
                yield f"data: {json.dumps(data, ensure_ascii=False)}\n\n"
                return

            # 分块发送（每3-5个字一块，模拟流畅感）
            chunk_size = 5
            for i in range(0, len(text), chunk_size):
                chunk = text[i:i+chunk_size]
                last_chunk = (i + chunk_size >= len(text))
                
                data = base_data.copy()
                data.update({
                    'text': chunk, 
                    'done': is_done if last_chunk else False
                })
                
                yield f"data: {json.dumps(data, ensure_ascii=False)}\n\n"
                
                # 增加极短的延迟（类似打字机）
                import time
                time.sleep(0.01)

        def _get_current_version_info():
            """获取当前 pair_id 的版本信息"""
            if not pair_id: return 1, 0
            try:
                c_data = storage.get_conversation(user_id, conv_id)
                for m in c_data.get('messages', []):
                    if m['role'] == 'assistant' and m.get('pair_id') == pair_id:
                        v_list = m.get('versions', [m['content']])
                        return len(v_list), m.get('active_index', 0)
            except: pass
            return 1, 0

        try:
            # 推送初始状态
            yield f"data: {json.dumps({'status': '正在分析您的问题...', 'conversation_id': conv_id}, ensure_ascii=False)}\n\n"
            
            # 步骤0: 意图分析 - 判断是单表还是多表查询
            logger.info("步骤0: 进行意图分析...")
            intent_info, intent_error = analyze_intent(message)
            
            if intent_error:
                logger.warning(f"意图分析失败: {intent_error}，降级到单表查询模式")
                intent_info = {'tables': [], 'is_multi_table': False, 'reason': '降级模式'}
            
            tables = intent_info.get('tables', [])
            is_multi_table = intent_info.get('is_multi_table', False)
            
            logger.info(f"意图分析结果: tables={tables}, is_multi_table={is_multi_table}, reason={intent_info.get('reason')}")
            print(f"【意图分析】表: {tables}, 多表: {is_multi_table}, 原因: {intent_info.get('reason')}")
            
            # 如果没有识别到表（可能是闲聊），使用原有的单表流程
            if not tables:
                logger.info("未识别到目标表，使用原有单表流程...")
                # 降级到原有的单表查询流程
                yield f"data: {json.dumps({'status': '正在理解您的问题...', 'conversation_id': conv_id}, ensure_ascii=False)}\n\n"
                
                # 1. 使用AI生成SQL
                logger.info("步骤1: 调用generate_sql生成查询语句...")
                sql_info, error = generate_sql(message)
                
                logger.info(f"generate_sql返回: sql_info={sql_info}, error={error}")
                
                # 检查是否有错误
                if error:
                    logger.error(f"生成SQL时出错: {error}")
                    response_text = f'抱歉，处理请求时出错: {error}'
                    _save_assistant_response(user_id, conv_id, pair_id, response_text, regenerate_pair_id)
                    v_count, a_idx = _get_current_version_info()
                    yield from _yield_stream_text(response_text, is_done=True, v_count=v_count, a_idx=a_idx)
                    return
                
                # 检查是否无法生成有效SQL
                is_unable, response_text = _is_unable_to_generate_sql(sql_info)
                if is_unable:
                    logger.warning(f"无法生成有效SQL: {response_text}")
                    _save_assistant_response(user_id, conv_id, pair_id, response_text, regenerate_pair_id)
                    v_count, a_idx = _get_current_version_info()
                    yield from _yield_stream_text(response_text, is_done=True, v_count=v_count, a_idx=a_idx)
                    return
                
                # 推送查询状态
                yield f"data: {json.dumps({'status': '正在检索相关数据...', 'conversation_id': conv_id}, ensure_ascii=False)}\n\n"
                
                # 2. 执行SQL查询
                sql_query = sql_info['sql']
                logger.info(f"步骤2: 执行SQL查询")
                logger.info(f"SQL语句: {sql_query}")
                
                print("\n" + "#"*50)
                print(f"【数据库流式查询】")
                print(f"执行 SQL: {sql_query}")
                
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    results, db_error = loop.run_until_complete(
                        db_service.execute_query(sql_query)
                    )
                finally:
                    loop.close()
                
            else:
                # 多表查询模式（包括单表识别的情况）
                if is_multi_table:
                    yield f"data: {json.dumps({'status': f'正在检索 {len(tables)} 个数据源...', 'conversation_id': conv_id}, ensure_ascii=False)}\n\n"
                else:
                    yield f"data: {json.dumps({'status': '正在检索相关数据...', 'conversation_id': conv_id}, ensure_ascii=False)}\n\n"
                
                print("\n" + "#"*50)
                print(f"【{'多表' if is_multi_table else '单表'}查询模式】目标表: {tables}")
                
                # 执行多表查询
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    results, query_errors = loop.run_until_complete(
                        _execute_multi_table_query(message, tables)
                    )
                    db_error = '; '.join(query_errors) if query_errors else None
                finally:
                    loop.close()
            
            print(f"查询结果: 返回 {len(results) if results else 0} 条记录")
            if db_error:
                print(f"数据库错误: {db_error}")
            print("#"*50 + "\n")
            
            logger.info(f"查询结果: 返回 {len(results) if results else 0} 条记录")
            if results:
                logger.info(f"结果: {results}")
            logger.info(f"数据库错误: {db_error}")
            
            if db_error and not results:
                logger.error(f"数据库查询失败: {db_error}")
                error_text = f"数据库查询失败: {db_error}"
                v_count, a_idx = _get_current_version_info()
                yield from _yield_stream_text(error_text, is_done=True, v_count=v_count, a_idx=a_idx)
                return
            
            # 3. 使用流式AI格式化结果
            logger.info(f"步骤3: 构建结果格式化提示词...")
            # 构建提示词
            from .cost_ai_prompt import RESULT_FORMAT_PROMPT
            if not results:
                results_text = "未找到相关数据"
                logger.warning("查询结果为空！")
            else:
                from decimal import Decimal
                simplified = []
                for r in results:
                    item = {}
                    # 定义核心关注的字段
                    core_keys = ['materialname', 'equipmentname', 'itname', 'servicename', 
                                'brand', 'specification', 'pretaxprice', 'afertaxprice']
                    
                    # 1. 尝试提取核心字段
                    for key in core_keys:
                        if key in r:
                            val = r[key]
                            if val is not None and val != "":
                                item[key] = float(val) if isinstance(val, Decimal) else val
                    
                    # 2. 如果核心字段太少（比如 AI 用了别名只返回了一个字段），把其他非内部字段也带上
                    if len(item) < 2:
                        for k, v in r.items():
                            if k not in core_keys and k not in ['id', 'status', 'created_at', 'updated_at', 'deleted_at']:
                                if v is not None and v != "":
                                    item[k] = float(v) if isinstance(v, Decimal) else v
                    
                    if item:
                        simplified.append(item)
                results_text = json.dumps(simplified, ensure_ascii=False, indent=2)
                logger.info(f"结果(用于AI格式化): {results_text}...")
            
            prompt = RESULT_FORMAT_PROMPT.format(question=message, results=results_text)
            logger.info(f"格式化提示词: {prompt}...")
            
            
            # 推送生成回答状态
            yield f"data: {json.dumps({'status': '正在生成回答...', 'conversation_id': conv_id}, ensure_ascii=False)}\n\n"
            
            # 流式输出
            for chunk in stream_ai_response(prompt):
                full_response.append(chunk)
                yield f"data: {json.dumps({'text': chunk, 'pair_id': pair_id}, ensure_ascii=False)}\n\n"
            
            # 保存完整AI回复
            complete_response = ''.join(full_response)
            logger.info(f"流式输出完成，完整内容: {complete_response}")
            if complete_response:
                _save_assistant_response(user_id, conv_id, pair_id, complete_response, regenerate_pair_id)
            
            # 获取更新后的消息状态（版本数等）
            versions_count, active_index = _get_current_version_info()

            # 发送完成标记
            yield f"data: {json.dumps({'done': True, 'conversation_id': conv_id, 'pair_id': pair_id, 'versions_count': versions_count, 'active_index': active_index}, ensure_ascii=False)}\n\n"
            
            logger.info(f"========== 流式请求处理完成 ==========\n")
                
        except Exception as e:
            error_text = f"处理请求时出错: {str(e)}"
            yield f"data: {json.dumps({'text': error_text, 'done': True, 'error': True}, ensure_ascii=False)}\n\n"
        
        # 最终结束标记
        yield "data: [DONE]\n\n"
    
    return Response(
        stream_with_context(generate()),
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache',
            'X-Accel-Buffering': 'no',  # 禁用Nginx缓冲
            'Connection': 'keep-alive'
        }
    )


@cost_ai_bp.route('/api/cost-ai/config', methods=['GET'])
def get_config():
    """
    获取造价AI前端配置
    
    返回前端需要知道的配置信息，如流式输出是否启用等。
    """
    from app.config import Config
    
    return jsonify({
        'success': True,
        'config': {
            'stream_enabled': Config.COST_AI_STREAM_ENABLED
        }
    })

