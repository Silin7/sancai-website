/**
 * Cost AI - UI 工具和初始化模块
 * 负责：用户信息加载、工具函数、UI交互、文件上传、下拉菜单等
 */

// ==================== 工具函数 ====================

// HTML转义工具函数
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// 获取当前时间
function getCurrentTime() {
    const now = new Date();
    return `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}`;
}

// 格式化日期
function formatDate(dateStr) {
    if (!dateStr) return '';
    const date = new Date(dateStr);
    const today = new Date();
    const isToday = date.getDate() === today.getDate() &&
        date.getMonth() === today.getMonth() &&
        date.getFullYear() === today.getFullYear();
    if (isToday) {
        return `${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}`;
    }
    return `${date.getMonth() + 1}/${date.getDate()}`;
}

// 滚动到底部
function scrollToBottom(force = false) {
    const c = document.getElementById('chat-container');
    if (!c) return;

    // 如果不是强制滚动，则检查是否已经接近底部
    // 阈值设为 100px
    const threshold = 100;
    const isNearBottom = c.scrollHeight - c.scrollTop - c.clientHeight < threshold;

    if (force || isNearBottom) {
        c.scrollTop = c.scrollHeight;
    }
}

// 复制消息
function copyMessage(btn) {
    const messageDiv = btn.closest('.chat-message-wrapper').querySelector('.chat-bubble-ai');
    const text = messageDiv.innerText;
    navigator.clipboard.writeText(text).then(() => {
        const originalIcon = btn.querySelector('i');
        originalIcon.className = 'fa fa-check';
        btn.style.color = '#10b981';
        setTimeout(() => {
            originalIcon.className = 'fa fa-copy';
            btn.style.color = '';
        }, 2000);
    });
}

// ==================== 统一菜单操作模块 ====================

/**
 * 统一的对话菜单操作模块
 * 提供统一接口供侧边栏菜单和顶部标题菜单调用
 */
const ConversationMenuActions = {
    // 执行重命名操作
    rename(convId, currentTitle) {
        openRenameModal(convId, currentTitle);
    },

    // 执行分享操作
    share(convId) {
        shareConversation(convId);
    },

    // 执行删除操作
    delete(convId) {
        deleteConversation(convId);
    },

    // 获取当前对话信息
    getCurrentConversation() {
        if (!currentConversationId) return null;
        const conv = conversationsCache.find(c => c.id === currentConversationId);
        return conv ? { id: conv.id, title: conv.title || '无标题' } : null;
    },

    // 菜单项配置
    getMenuItems() {
        return [
            { key: 'rename', icon: 'fa-pencil', label: '重命名', action: 'rename' },
            { key: 'share', icon: 'fa-share-alt', label: '分享对话', action: 'share' },
            { key: 'delete', icon: 'fa-trash-o', label: '删除对话', action: 'delete', danger: true }
        ];
    },

    /**
     * 生成菜单 HTML
     * @param {string} convId - 对话 ID
     * @param {string} currentTitle - 当前标题
     * @param {string} styleType - 样式类型：'sidebar'(侧边栏) 或 'topbar'(顶部标题)
     * @param {object} styleConfig - 样式配置（仅 sidebar 需要）
     * @returns {string} 菜单按钮 HTML
     */
    renderMenuItems(convId, currentTitle, styleType, styleConfig = {}) {
        const items = this.getMenuItems();

        if (styleType === 'topbar') {
            // 顶部标题栏样式
            return items.map((item, index) => {
                const dangerClass = item.danger ? ' delete' : '';
                return `
                    <button class="chat-title-menu-item${dangerClass}" data-action="${item.action}" data-conv-id="${convId}" data-title="${escapeHtml(currentTitle)}">
                        <i class="fa ${item.icon}"></i>
                        <span>${item.label}</span>
                    </button>
                `;
            }).join('');
        } else {
            // 侧边栏样式
            const { menuBtnClass, menuBtnStyle, menuBtnInnerStyle, separatorStyle } = styleConfig;
            return items.map((item, index) => {
                const separator = index > 0 ? separatorStyle : '';
                return `
                    <button onclick="ConversationMenuActions.handleAction('${item.action}', '${convId}', '${escapeHtml(currentTitle)}')"
                            class="flex items-center w-full text-left px-3 py-1.5 text-xs transition-colors ${menuBtnClass}"
                            style="${menuBtnStyle} margin: 0 !important; ${separator}">
                        <i class="fa ${item.icon} mr-2 opacity-70" style="${menuBtnInnerStyle}"></i>
                        <span style="${menuBtnInnerStyle}">${item.label}</span>
                    </button>
                `;
            }).join('');
        }
    },

    /**
     * 统一处理菜单操作
     * @param {string} action - 操作类型
     * @param {string} convId - 对话 ID
     * @param {string} currentTitle - 当前标题
     */
    handleAction(action, convId, currentTitle) {
        switch (action) {
            case 'rename':
                this.rename(convId, currentTitle);
                break;
            case 'share':
                this.share(convId);
                break;
            case 'delete':
                this.delete(convId);
                break;
        }
    }
};

// ==================== 全局状态 ====================
let currentConversationId = null;
let currentFiles = [];
let userAvatar = "https://ui-avatars.com/api/?name=User&background=random"; // 默认用户头像
let conversationsCache = []; // 缓存对话列表数据

// ==================== 用户信息加载 ====================

// 加载用户信息
async function loadUserInfo() {
    try {
        const res = await fetch('/api/user/info');
        const data = await res.json();
        if (data.success) {
            // 更新头部
            const usernameEl = document.getElementById('username');
            const avatarEl = document.getElementById('user-avatar');
            if (usernameEl) usernameEl.textContent = data.username;
            if (avatarEl) avatarEl.innerHTML = data.avatar;
            // 直接存储头像内容 (SVG 或 Emoji 字符串)
            userAvatar = data.avatar || userAvatar;
            // 如果需要也可以存储头像类型，但对于渲染字符串来说已经足够了
            if (data.avatar_type === 'emoji') {
                // 如果需要特定的 Emoji 样式处理
            }
        }
    } catch (e) {
        console.error('Fetch user info error:', e);
    }
}

// ==================== 文件上传相关 ====================

// 处理文件上传
function handleFileUpload(input) {
    const files = Array.from(input.files);

    files.forEach(file => {
        if (file.size > 10 * 1024 * 1024) {
            alert('文件大小不能超过10MB');
            return;
        }

        if (!currentFiles.find(f => f.name === file.name)) {
            currentFiles.push(file);
        }
    });

    updateFilePreviewArea();
}

// 更新文件预览区域
function updateFilePreviewArea() {
    const previewArea = document.getElementById('file-preview-area');
    previewArea.innerHTML = '';

    if (currentFiles.length > 0) {
        previewArea.classList.add('active');
        currentFiles.forEach(file => {
            const tag = document.createElement('div');
            tag.className = 'file-tag';
            tag.innerHTML = `
        <i class="fa fa-file"></i>
        <span>${escapeHtml(file.name)}</span>
        <i class="fa fa-times file-remove" onclick="removeFile('${file.name}')"></i>
      `;
            previewArea.appendChild(tag);
        });
    } else {
        previewArea.classList.remove('active');
    }
}

// 移除文件
function removeFile(fileName) {
    currentFiles = currentFiles.filter(f => f.name !== fileName);
    updateFilePreviewArea();
}

// ==================== 聊天标题管理 ====================

// 更新聊天标题显示
function updateChatTitle(title) {
    const chatTitleText = document.getElementById('chatTitleText');
    const chatTitleContainer = document.getElementById('chatTitleContainer');

    if (chatTitleText && chatTitleContainer) {
        if (currentConversationId) {
            chatTitleText.textContent = title || '新对话';
            chatTitleContainer.style.display = 'flex';
        } else {
            chatTitleContainer.style.display = 'none';
        }
    }
}

// ==================== 输入框相关 ====================

// 设置输入框内容
function setInput(text) {
    const input = document.getElementById('user-input');
    if (input) {
        input.value = text;
        input.dispatchEvent(new Event('input')); // 触发自动高度调整
        input.focus();
    }
}

// ==================== 初始化 ====================

async function init() {
    if (window.__ai_initialized) return;
    window.__ai_initialized = true;
    // console.log('Initializing...');
    loadUserInfo();

    // 获取当前URL路径
    const currentPath = window.location.pathname;
    // console.log('Current path:', currentPath);

    // 检查是否是对话页面
    const pathParts = currentPath.split('/').filter(part => part !== '');
    // console.log('Path parts:', pathParts);

    let urlConvId = null;
    if (pathParts.length >= 2 && pathParts[0] === 'cost-ai' && pathParts[1]) {
        urlConvId = pathParts[1];
    }

    // console.log('URL conv ID:', urlConvId);

    // 先渲染对话列表，获取对话数据
    await renderConversationList();

    // 检查是否是具体的对话页面
    const isConversationPage = urlConvId && urlConvId !== 'cost-ai' && urlConvId !== '';
    // console.log('Is conversation page:', isConversationPage);

    if (isConversationPage) {
        // console.log('Loading conversation:', urlConvId);
        // 统一使用原始 8 位 ID
        const fullConvId = urlConvId;
        // console.log('Full conv ID:', fullConvId);

        // 从缓存的对话列表中查找标题
        const conversation = conversationsCache.find(conv => conv.id === fullConvId);

        if (conversation) {
            // 直接使用缓存中的标题
            await selectConversation(fullConvId, conversation.title || '新对话');
        } else {
            // 对话不存在于列表中，显示新聊天界面
            console.log('Conversation not found in list, showing new chat UI');
            showNewChatUI();
        }
    } else {
        // console.log('Showing new chat UI');
        showNewChatUI();
    }
}

// ==================== 事件监听器设置 ====================

// 在 DOM 加载完成后设置事件监听器
function setupEventListeners() {
    // Note: 登出功能已移除，系统自动管理用户session

    // 用户下拉菜单功能
    const userInfo = document.getElementById('userInfo');
    const userDropdownMenu = document.getElementById('userDropdownMenu');
    const userDropdownIcon = document.querySelector('.user-dropdown');

    if (userInfo && userDropdownMenu && userDropdownIcon) {
        // 切换下拉菜单显示/隐藏
        userInfo.addEventListener('click', function (e) {
            e.stopPropagation();
            userDropdownMenu.classList.toggle('show');
            if (userDropdownMenu.classList.contains('show')) {
                userDropdownIcon.style.transform = 'rotate(180deg)';
            } else {
                userDropdownIcon.style.transform = 'rotate(0)';
            }
        });

        // 点击页面其他区域关闭下拉菜单
        document.addEventListener('click', function () {
            userDropdownMenu.classList.remove('show');
            userDropdownIcon.style.transform = 'rotate(0)';
        });

        // 阻止下拉菜单内部点击事件冒泡
        userDropdownMenu.addEventListener('click', function (e) {
            e.stopPropagation();
        });
    }

    // 聊天标题下拉菜单功能
    const chatTitleContainer = document.getElementById('chatTitleContainer');
    const chatTitleMenu = document.getElementById('chatTitleMenu');
    const chatTitleDropdownIcon = document.querySelector('.chat-title-dropdown-icon');

    // 关闭菜单的辅助函数
    function closeChatTitleMenu() {
        if (chatTitleMenu) chatTitleMenu.classList.remove('show');
        if (chatTitleDropdownIcon) chatTitleDropdownIcon.style.transform = 'rotate(0)';
    }

    // 切换聊天标题下拉菜单
    if (chatTitleContainer && chatTitleMenu && chatTitleDropdownIcon) {
        chatTitleContainer.addEventListener('click', function (e) {
            e.stopPropagation();

            // 动态生成菜单内容
            const conv = ConversationMenuActions.getCurrentConversation();
            if (conv) {
                chatTitleMenu.innerHTML = ConversationMenuActions.renderMenuItems(conv.id, conv.title, 'topbar');
            }

            chatTitleMenu.classList.toggle('show');
            if (chatTitleMenu.classList.contains('show')) {
                chatTitleDropdownIcon.style.transform = 'rotate(180deg)';
            } else {
                chatTitleDropdownIcon.style.transform = 'rotate(0)';
            }
        });

        // 点击页面其他区域关闭聊天标题菜单
        document.addEventListener('click', function () {
            closeChatTitleMenu();
        });

        // 使用事件委托处理菜单项点击
        chatTitleMenu.addEventListener('click', function (e) {
            e.stopPropagation();

            // 查找被点击的菜单项按钮
            const menuItem = e.target.closest('[data-action]');
            if (menuItem) {
                const action = menuItem.dataset.action;
                const convId = menuItem.dataset.convId;
                const title = menuItem.dataset.title;

                ConversationMenuActions.handleAction(action, convId, title);
                closeChatTitleMenu();
            }
        });
    }

    // 文件上传监听器
    const fileUpload = document.getElementById('file-upload');
    if (fileUpload) {
        fileUpload.addEventListener('change', (e) => handleFileUpload(e.target));
    }
}

// 页面加载时初始化
document.addEventListener('DOMContentLoaded', () => {
    init();
    setupEventListeners();
});

if (document.readyState === 'complete' || document.readyState === 'interactive') {
    init();
    setupEventListeners();
}
