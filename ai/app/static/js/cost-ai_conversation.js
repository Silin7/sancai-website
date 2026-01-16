/**
 * Cost AI - 对话管理模块
 * 负责：对话列表加载、对话选择、创建对话、删除对话、重命名对话
 */

// ==================== 对话列表管理 ====================

// 加载对话列表并渲染
async function renderConversationList() {
    // console.log('Rendering conversation list, currentConversationId:', currentConversationId);
    try {
        const res = await fetch('/api/cost-ai/conversations');
        // console.log('Conversations fetch status:', res.status);
        const data = await res.json();
        // console.log('Conversations data:', data);

        if (data.success) {
            // 存储到全局缓存
            conversationsCache = data.conversations || [];

            const listContainer = document.getElementById('conversation-list');
            listContainer.innerHTML = '';

            if (data.conversations.length === 0) {
                listContainer.innerHTML = '<div class="text-center text-xs text-white/60 py-4">暂无历史对话</div>';
            }

            data.conversations.forEach(conv => {
                const item = document.createElement('div');
                // 检查激活状态
                const isActive = conv.id === currentConversationId;
                // console.log('Conversation:', conv.id, 'isActive:', isActive);

                // 基础类样式
                let classes = 'px-3 rounded-lg cursor-pointer transition-colors duration-200 relative group flex items-center shrink-0';
                // 内联样式确保高度
                let itemStyle = 'height: 35px; min-height: 35px;';

                let iconClass = '';
                let menuContainerStyle = '';
                let menuBtnClass = '';
                let menuBtnStyle = '';

                // 深度样式变量
                let iconInnerStyle = '';
                let menuBtnInnerStyle = '';

                if (isActive) {
                    // 激活状态: 白色背景, 红色文字 (#a6171c)
                    classes += ' bg-white shadow-sm';
                    itemStyle += ' color: #a6171c;';

                    // 图标: 激活状态下为红色
                    iconClass = 'hover:bg-black/5';
                    iconInnerStyle = 'color: #a6171c !important;';

                    // 菜单: 标准白色背景, 红色文字
                    menuContainerStyle = 'background-color: #ffffff;';
                    menuBtnClass = 'hover:bg-gray-100';
                    menuBtnStyle = 'color: #a6171c;';
                    menuBtnInnerStyle = 'color: #a6171c !important;';
                    separatorStyle = 'border-top: 1px solid rgba(0,0,0,0.05);';
                } else {
                    // 未激活状态: 透明, 白色文字
                    classes += ' hover:bg-white/10';
                    itemStyle += ' color: rgba(255,255,255,0.9);';

                    // 图标: 白色
                    iconClass = 'hover:bg-white/20';
                    iconInnerStyle = 'color: #ffffff !important;';

                    // 菜单: 红色背景, 白色文字
                    menuContainerStyle = 'background-color: #a6171c; border: 1px solid rgba(255,255,255,0.2);';
                    menuBtnClass = 'hover:bg-white/20';
                    menuBtnStyle = 'color: #ffffff;';
                    menuBtnInnerStyle = 'color: #ffffff !important;';
                    separatorStyle = 'border-top: 1px solid rgba(255,255,255,0.2);';
                }


                item.className = classes;
                item.style.cssText = itemStyle;
                item.dataset.id = conv.id;

                item.innerHTML = `
        <div class="flex-1 min-w-0 flex items-center h-full relative">
          <h3 class="text-sm font-medium truncate flex-1 select-none leading-none pr-2" style="line-height: normal;">${escapeHtml(conv.title || '无标题')}</h3>
          
          <!-- 三点菜单按钮 -->
          <!-- 使用 flex 项目代替绝对定位以确保居中 -->
          <div role="button" class="flex-none opacity-0 group-hover:opacity-100 transition-opacity w-8 h-6 flex items-center justify-center rounded-full cursor-pointer ${iconClass}"
                  style="margin-right: -4px;"
                  title="更多选项"
                  onclick="event.stopPropagation(); showContextMenu(event, '${conv.id}', '${escapeHtml(conv.title || '无标题')}')">
            <div class="flex" style="${iconInnerStyle} gap: 2px;">
                <span class="block rounded-full" style="width: 5px; height: 5px; background-color: ${isActive ? '#a6171c' : '#ffffff'};"></span>
                <span class="block rounded-full" style="width: 5px; height: 5px; background-color: ${isActive ? '#a6171c' : '#ffffff'};"></span>
                <span class="block rounded-full" style="width: 5px; height: 5px; background-color: ${isActive ? '#a6171c' : '#ffffff'};"></span>
            </div>
          </div>
          
          <!-- 此项目的上下文菜单 -->
          <div id="menu-${conv.id}" class="context-menu shadow-xl" style="${menuContainerStyle}" onclick="event.stopPropagation()">
            ${ConversationMenuActions.renderMenuItems(conv.id, conv.title || '无标题', 'sidebar', { menuBtnClass, menuBtnStyle, menuBtnInnerStyle, separatorStyle })}
          </div>
        </div>
    `;
                item.addEventListener('click', () => selectConversation(conv.id, conv.title || '无标题'));
                listContainer.appendChild(item);
            });

            // 渲染完成后，如果当前有选中的对话，强制更新顶部标题
            if (currentConversationId) {
                const currentConv = conversationsCache.find(conv => conv.id === currentConversationId);
                if (currentConv) {
                    updateChatTitle(currentConv.title || '新对话');
                }
            }
        }
    } catch (e) {
        console.error('Load conversations error', e);
    } finally {
        isRendering = false;
    }
}

// ==================== 对话选择 ====================

// 显示新聊天UI
function showNewChatUI() {
    // console.log('Showing New Chat UI');
    currentConversationId = null;
    document.getElementById('chat-container').innerHTML = '';
    const welcomeMsg = document.getElementById('welcome-message');
    if (welcomeMsg) {
        welcomeMsg.classList.remove('hidden');
        welcomeMsg.style.display = 'flex'; // 强制显示
    }

    // 更新 URL 为基础路径
    const currentPath = window.location.pathname;
    // console.log('Current path in showNewChatUI:', currentPath);
    if (currentPath !== '/cost-ai' && !currentPath.endsWith('/cost-ai')) {
        // console.log('Updating URL to /cost-ai');
        window.history.pushState({}, '', '/cost-ai');
    }

    // 隐藏聊天标题
    updateChatTitle('');

    // 刷新列表以清除选中高亮
    renderConversationList();
}

// 选择对话
async function selectConversation(convId, title) {
    // console.log('Selecting conversation:', convId);

    // 1. 即时反馈：立即更新侧边栏样式，提升响应感
    const allItems = document.querySelectorAll('.conversation-item');
    allItems.forEach(item => {
        if (item.getAttribute('onclick')?.includes(`'${convId}'`)) {
            item.classList.add('active');
        } else {
            item.classList.remove('active');
        }
    });

    currentConversationId = convId;

    // 更新 URL，去除 conv_ 前缀
    const shortId = convId.startsWith('conv_') ? convId.substring(5) : convId;
    window.history.pushState({ id: convId }, '', `/cost-ai/${shortId}`);

    // 直接使用传递的标题更新UI
    updateChatTitle(title || '新对话');

    // 2. 异步执行：重新渲染列表（确保服务端状态同步）和加载消息
    await renderConversationList();
    await loadConversationMessages(convId);
}

// ==================== 上下文菜单 ====================

let currentMenuId = null;
let targetRenameId = null;

// 显示上下文菜单
function showContextMenu(e, convId, currentTitle) {
    // 先关闭任何打开的菜单
    closeContextMenu();

    const menu = document.getElementById(`menu-${convId}`);
    if (menu) {
        menu.style.display = 'block';
        currentMenuId = `menu-${convId}`;
    }

    // 设置点击外部关闭监听器
    setTimeout(() => {
        document.addEventListener('click', closeContextMenu);
    }, 0);
}

// 关闭上下文菜单
function closeContextMenu() {
    if (currentMenuId) {
        const menu = document.getElementById(currentMenuId);
        if (menu) menu.style.display = 'none';
        currentMenuId = null;
    }
    document.removeEventListener('click', closeContextMenu);
}

// ==================== 重命名对话 ====================

// 打开重命名模态框
function openRenameModal(convId, currentTitle) {
    closeContextMenu(); // 确保菜单已关闭
    targetRenameId = convId;
    const input = document.getElementById('rename-input');
    input.value = currentTitle;
    document.getElementById('rename-modal').classList.remove('hidden');
    input.focus();

    // 回车提交
    input.onkeydown = (e) => {
        if (e.key === 'Enter') submitRename();
        if (e.key === 'Escape') closeRenameModal();
    };
}

// 关闭重命名模态框
function closeRenameModal() {
    document.getElementById('rename-modal').classList.add('hidden');
    targetRenameId = null;
}

// 提交重命名
async function submitRename() {
    if (!targetRenameId) return;

    const newTitle = document.getElementById('rename-input').value.trim();
    if (!newTitle) {
        alert('标题不能为空');
        return;
    }

    try {
        const res = await fetch(`/api/cost-ai/conversations/${targetRenameId}/title`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: newTitle })
        });
        const data = await res.json();

        if (data.success) {
            closeRenameModal();
            // 重新渲染列表，内部会自动同步顶部标题
            renderConversationList();
        } else {
            alert('修改失败: ' + data.error);
        }
    } catch (e) {
        console.error(e);

        // 检测是否是页面刷新/卸载导致的错误
        const isNavigationError =
            e.name === 'AbortError' ||
            e.name === 'TypeError' && (
                e.message.includes('Failed to fetch') ||
                e.message.includes('NetworkError') ||
                e.message.includes('cancelled') ||
                e.message.includes('aborted')
            );

        // 只有在不是页面刷新/卸载导致的错误时才弹出提示
        if (!isNavigationError) {
            alert('网络错误: ' + e.message);
        }
    }
}

// ==================== 删除对话 ====================

// 删除对话
async function deleteConversation(convId) {
    // 防止冒泡到项目点击事件
    if (!confirm('确定要删除这个对话吗？')) return;

    closeContextMenu();

    try {
        const res = await fetch(`/api/cost-ai/conversations/${convId}`, {
            method: 'DELETE'
        });
        const data = await res.json();
        if (data.success) {
            // 从列表中移除或重新加载
            // 如果删除当前对话，清除聊天或选择另一个？
            if (currentConversationId === convId) {
                showNewChatUI();
            }
            renderConversationList();
        } else {
            alert('删除失败: ' + (data.error || '未知错误'));
        }
    } catch (e) {
        console.error(e);

        // 检测是否是页面刷新/卸载导致的错误
        const isNavigationError =
            e.name === 'AbortError' ||
            e.name === 'TypeError' && (
                e.message.includes('Failed to fetch') ||
                e.message.includes('NetworkError') ||
                e.message.includes('cancelled') ||
                e.message.includes('aborted')
            );

        // 只有在不是页面刷新/卸载导致的错误时才弹出提示
        if (!isNavigationError) {
            alert('网络错误');
        }
    }
}

// ==================== 新对话按钮 ====================

// 设置新对话按钮监听器
document.addEventListener('DOMContentLoaded', () => {
    const newConvBtn = document.getElementById('new-conversation');
    if (newConvBtn) {
        newConvBtn.addEventListener('click', () => {
            showNewChatUI();
        });
    }
});

// ==================== 分享对话 ====================

// 分享对话
async function shareConversation(convId) {
    closeContextMenu(); // 关闭菜单

    // 移除 conv_ 前缀（如果有）
    const shortId = convId.startsWith('conv_') ? convId.substring(5) : convId;

    try {
        const res = await fetch(`/api/cost-ai/share/${shortId}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        const data = await res.json();

        if (data.success) {
            const fullUrl = window.location.origin + data.share_url;
            showShareModal(fullUrl, data.is_new);
        } else {
            alert('分享失败: ' + (data.error || '未知错误'));
        }
    } catch (e) {
        console.error('Share error:', e);

        // 检测是否是页面刷新/卸载导致的错误
        const isNavigationError =
            e.name === 'AbortError' ||
            e.name === 'TypeError' && (
                e.message.includes('Failed to fetch') ||
                e.message.includes('NetworkError') ||
                e.message.includes('cancelled') ||
                e.message.includes('aborted')
            );

        if (!isNavigationError) {
            alert('网络错误，无法生成分享链接');
        }
    }
}

// 显示分享弹窗
function showShareModal(shareUrl, isNew) {
    // 检查弹窗是否已存在，如果不存在则创建
    let modal = document.getElementById('share-modal');
    if (!modal) {
        const modalHtml = `
            <div id="share-modal" class="modal-overlay fixed inset-0 z-50 hidden flex items-center justify-center">
                <div class="bg-white rounded-xl shadow-2xl p-6 transform transition-all scale-100" style="width: 500px;">
                    <h3 class="text-lg font-bold text-gray-900 mb-2">
                        <i class="fa fa-share-alt text-[#a6171c] mr-2"></i>分享对话
                    </h3>
                    <p class="text-sm text-gray-500 mb-4" id="share-modal-subtitle">分享链接已生成，复制后发送给他人即可查看</p>
                    
                    <div class="flex items-center space-x-2 mb-4">
                        <input type="text" id="share-url-input" readonly
                            class="flex-1 px-3 py-2 border border-gray-300 rounded-lg bg-gray-50 text-sm text-gray-700"
                            style="font-family: monospace;">
                        <button onclick="copyShareUrl()" 
                            class="px-4 py-2 bg-[#a6171c] text-white rounded-lg hover:bg-[#8a1217] transition-colors"
                            id="copy-share-btn">
                            <i class="fa fa-copy mr-1"></i>复制
                        </button>
                    </div>
                    
                    <div class="text-xs text-gray-400 mb-4">
                        <i class="fa fa-info-circle mr-1"></i> 任何人通过此链接都可以查看对话内容
                    </div>
                    
                    <div class="flex justify-end">
                        <button onclick="closeShareModal()"
                            class="px-4 py-2 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors">关闭</button>
                    </div>
                </div>
            </div>`;
        document.body.insertAdjacentHTML('beforeend', modalHtml);
        modal = document.getElementById('share-modal');
    }

    // 更新内容
    const urlInput = document.getElementById('share-url-input');
    const subtitle = document.getElementById('share-modal-subtitle');
    const copyBtn = document.getElementById('copy-share-btn');

    urlInput.value = shareUrl;
    subtitle.textContent = isNew ? '分享链接已生成，复制后发送给他人即可查看' : '该对话已有分享链接';
    copyBtn.innerHTML = '<i class="fa fa-copy mr-1"></i>复制';

    // 显示弹窗
    modal.classList.remove('hidden');
}

// 关闭分享弹窗
function closeShareModal() {
    const modal = document.getElementById('share-modal');
    if (modal) {
        modal.classList.add('hidden');
    }
}

// 复制分享链接
function copyShareUrl() {
    const urlInput = document.getElementById('share-url-input');
    const copyBtn = document.getElementById('copy-share-btn');

    urlInput.select();
    urlInput.setSelectionRange(0, 99999); // 移动端兼容

    try {
        navigator.clipboard.writeText(urlInput.value).then(() => {
            copyBtn.innerHTML = '<i class="fa fa-check mr-1"></i>已复制';
            setTimeout(() => {
                copyBtn.innerHTML = '<i class="fa fa-copy mr-1"></i>复制';
            }, 2000);
        });
    } catch (e) {
        // 降级方案
        document.execCommand('copy');
        copyBtn.innerHTML = '<i class="fa fa-check mr-1"></i>已复制';
        setTimeout(() => {
            copyBtn.innerHTML = '<i class="fa fa-copy mr-1"></i>复制';
        }, 2000);
    }
}
