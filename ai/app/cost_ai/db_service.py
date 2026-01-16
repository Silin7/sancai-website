import asyncio
import asyncpg
from app.config import Config

# 连接池
_pool = None
_pool_error = None  # 记录连接池创建时的错误

async def get_pool():
    """获取数据库连接池"""
    global _pool, _pool_error
    
    # 获取当前运行的事件循环
    try:
        current_loop = asyncio.get_running_loop()
    except RuntimeError:
        # 如果没有运行中的循环（不应该发生，因为此函数是async的）
        current_loop = asyncio.get_event_loop()

    if _pool is not None:
        # 检查已存在的连接池是否属于当前的事件循环
        # asyncpg.Pool 对象内部维护了一个 _loop 引用
        if hasattr(_pool, '_loop') and _pool._loop != current_loop:
            print(f"[DB] 检测到事件循环变更，重置连接池。旧循环: {id(_pool._loop)}, 新循环: {id(current_loop)}")
            # 注意：不要尝试关闭旧循环中的连接池，因为它可能已经失效
            _pool = None
            _pool_error = None
        else:
            return _pool
    
    # 如果之前创建失败过且循环没变，返回之前的错误
    if _pool_error is not None and _pool is None:
        raise ConnectionError(f"数据库连接池创建失败: {_pool_error}")
    
    try:
        _pool = await asyncpg.create_pool(
            host=Config.COST_DB_HOST,
            port=Config.COST_DB_PORT,
            user=Config.COST_DB_USER,
            password=Config.COST_DB_PASSWORD,
            database=Config.COST_DB_NAME,
            min_size=1,
            max_size=5,
            timeout=30
        )
        print(f"[DB] 连接池创建成功 (Loop: {id(current_loop)})")
        _pool_error = None
        return _pool
    except Exception as e:
        _pool_error = str(e)
        print(f"[DB] 连接池创建失败: {e}")
        raise ConnectionError(f"数据库连接池创建失败: {e}")

async def execute_query(sql: str) -> tuple:
    """
    执行SQL查询
    
    Returns:
        tuple: (results, error) - results为字典列表，error为错误信息
    """
    global _pool, _pool_error
    
    try:
        pool = await get_pool()
        
        if pool is None:
            return None, "数据库连接池未初始化"
        
        async with pool.acquire() as conn:
            rows = await conn.fetch(sql)
            # 转换为字典列表
            results = [dict(row) for row in rows]
            return results, None
    except ConnectionError as e:
        return None, str(e)
    except asyncpg.PostgresError as e:
        return None, f"SQL执行错误: {e}"
    except Exception as e:
        # 如果遇到连接或循环相关错误，重置状态以便下次重试
        error_msg = str(e).lower()
        if any(kw in error_msg for kw in ["connect", "connection", "loop", "operation"]):
            print(f"[DB] 发生致命错误，重置连接池状态: {e}")
            _pool = None
            _pool_error = None
        return None, str(e)

async def close_pool():
    """关闭连接池"""
    global _pool
    if _pool:
        await _pool.close()
        _pool = None
