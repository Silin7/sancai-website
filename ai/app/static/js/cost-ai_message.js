/**
 * Cost AI - 消息管理模块
 * 负责：加载历史消息、发送消息、渲染消息、加载指示器
 * 支持：SSE流式输出（类似ChatGPT打字机效果）
 */

// ==================== 流式输出配置 ====================

// 流式输出开关（页面加载时从后端获取）
let streamEnabled = false;

// AI头像SVG（复用于多处）
const aiAvatarSvg = `
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad_ai" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#f093fb;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#f5576c;stop-opacity:1" />
        </linearGradient>
    </defs>
    <circle cx="50" cy="50" r="50" fill="url(#grad_ai)"/>
    <circle cx="50" cy="38" r="15" fill="#ffffff" opacity="0.9"/>
    <rect x="30" y="58" width="40" height="38" rx="10" fill="#ffffff" opacity="0.9"/>  
</svg>`;

// 获取流式配置
async function fetchStreamConfig() {
    try {
        const res = await fetch('/api/cost-ai/config');
        const data = await res.json();
        if (data.success && data.config) {
            streamEnabled = data.config.stream_enabled || false;
            // console.log('流式输出配置:', streamEnabled ? '已启用' : '已禁用');
        }
    } catch (e) {
        // console.warn('获取流式配置失败，使用默认值(非流式):', e);
        streamEnabled = false;
    }
}

// 页面加载时获取配置
document.addEventListener('DOMContentLoaded', fetchStreamConfig);

// ==================== 流式消息渲染 ====================

/**
 * 创建流式AI消息气泡（空的，用于逐字填充）
 * 返回气泡内容元素的引用，用于后续追加文本
 */
function createStreamingAiBubble(container) {
    const wrapper = document.createElement('div');
    wrapper.className = 'chat-message-wrapper justify-start';
    wrapper.id = 'streaming-message';

    wrapper.innerHTML = `
        <div class="chat-avatar mr-2">
            <div class="w-full h-full overflow-hidden" style="border-radius: 4px;">
                ${aiAvatarSvg}
            </div>
        </div>
        <div class="flex flex-col items-start" style="max-width: 60%;">
            <div class="chat-bubble-ai" id="streaming-bubble-content">
                <span class="streaming-cursor"></span>
            </div>
            <div class="flex items-center space-x-3 chat-time" style="visibility: hidden;" id="streaming-time">
                <span></span>
            </div>
        </div>
    `;

    container.appendChild(wrapper);
    scrollToBottom(true); // 初始气泡创建，通常是新消息，强制滚动

    return document.getElementById('streaming-bubble-content');
}

//向流式气泡追加文本
function appendToStreamingBubble(bubble, text) {
    if (!bubble) return;

    // 移除光标，追加文本，再添加光标
    const cursor = bubble.querySelector('.streaming-cursor');
    if (cursor) cursor.remove();

    // 处理换行符
    const formattedText = escapeHtml(text).replace(/\n/g, '<br>');
    bubble.insertAdjacentHTML('beforeend', formattedText);

    // 重新添加光标
    bubble.insertAdjacentHTML('beforeend', '<span class="streaming-cursor"></span>');

    scrollToBottom(); // 流式追加：不带参数，使用智能滚动逻辑
}
/**
 * 完成流式消息（移除光标，显示时间、复制按钮、重新发起按钮和分页）
 */
function finalizeStreamingBubble(time, pairId, versionsCount = 1, activeIndex = 0, targetWrapper = null) {
    const wrapper = targetWrapper || document.getElementById('streaming-message');
    if (!wrapper) {
        // 如果没有 streaming-message，可能是非流式，或者是特殊的加载状态
        const loadingIndicator = document.getElementById('loading-indicator');
        if (loadingIndicator) {
            const timeEl = loadingIndicator.querySelector('.chat-time');
            if (timeEl) {
                timeEl.style.visibility = 'visible';
                const showPagination = versionsCount > 1;
                timeEl.innerHTML = `
                    <span>${time}</span>
                    <button class="text-gray-400 hover:text-gray-600 transition-colors" title="复制" onclick="copyMessage(this)">
                        <i class="fa fa-copy"></i>
                    </button>
                    <button class="text-gray-400 hover:text-gray-600 transition-colors regenerate-btn" title="重新回答" onclick="regenerateMessage(this)">
                        <i class="fa fa-refresh"></i>
                    </button>
                    <div class="pagination-controls flex items-center space-x-1 ${showPagination ? '' : 'hidden'}">
                        <button onclick="switchMessageVersion(this, -1)" class="text-gray-400 hover:text-gray-600"><i class="fa fa-chevron-left text-xs"></i></button>
                        <span class="page-text text-xs text-gray-500">${activeIndex + 1}/${versionsCount}</span>
                        <button onclick="switchMessageVersion(this, 1)" class="text-gray-400 hover:text-gray-600"><i class="fa fa-chevron-right text-xs"></i></button>
                    </div>
                `;
            }
            loadingIndicator.removeAttribute('id');
        }
        return;
    }

    // 设置 pairId
    if (pairId) wrapper.setAttribute('data-pair-id', pairId);

    // 移除光标
    const bubble = wrapper.querySelector('.chat-bubble-ai');
    if (bubble) {
        const cursor = bubble.querySelector('.streaming-cursor');
        if (cursor) cursor.remove();
    }

    // 显示时间及控制按钮
    const timeEl = wrapper.querySelector('.chat-time');
    if (timeEl) {
        timeEl.style.visibility = 'visible';
        const showPagination = versionsCount > 1;

        timeEl.innerHTML = `
            <span>${time}</span>
            <button class="text-gray-400 hover:text-gray-600 transition-colors" title="复制" onclick="copyMessage(this)">
                <i class="fa fa-copy"></i>
            </button>
            <button class="text-gray-400 hover:text-gray-600 transition-colors regenerate-btn" title="重新回答" onclick="regenerateMessage(this)">
                <i class="fa fa-refresh"></i>
            </button>
            <div class="pagination-controls flex items-center space-x-1 ${showPagination ? '' : 'hidden'}">
                <button onclick="switchMessageVersion(this, -1)" class="text-gray-400 hover:text-gray-600"><i class="fa fa-chevron-left text-xs"></i></button>
                <span class="page-text text-xs text-gray-500">${activeIndex + 1}/${versionsCount}</span>
                <button onclick="switchMessageVersion(this, 1)" class="text-gray-400 hover:text-gray-600"><i class="fa fa-chevron-right text-xs"></i></button>
            </div>
        `;
    }

    // 移除ID，允许创建下一个流式消息
    if (wrapper.id === 'streaming-message') {
        wrapper.removeAttribute('id');
        const bubbleContent = wrapper.querySelector('#streaming-bubble-content');
        if (bubbleContent) bubbleContent.removeAttribute('id');
        const timeContent = wrapper.querySelector('#streaming-time');
        if (timeContent) timeContent.removeAttribute('id');
    }
}



// 加载对话的历史消息
async function loadConversationMessages(convId, forceScroll = true) {
    // console.log('Loading messages for conversation:', convId);
    try {
        const res = await fetch(`/api/cost-ai/conversations/${convId}`);
        // console.log('Fetch response status:', res.status);
        const data = await res.json();
        // console.log('Response data:', data);

        if (data.success) {
            // 只在有明确标题时才更新，避免用默认值覆盖已设置的标题
            if (data.title) {
                updateChatTitle(data.title);
            }

            const chatContainer = document.getElementById('chat-container');
            chatContainer.innerHTML = '';

            // 切换欢迎消息显示
            const messages = data.messages || [];
            // console.log('Messages loaded:', messages.length);

            const welcomeMsg = document.getElementById('welcome-message');
            if (messages.length === 0) {
                if (welcomeMsg) {
                    welcomeMsg.classList.remove('hidden');
                    welcomeMsg.style.display = 'flex';
                }
            } else {
                if (welcomeMsg) {
                    welcomeMsg.classList.add('hidden');
                    welcomeMsg.style.display = 'none';
                }
            }

            messages.forEach((msg, idx) => {
                if (msg.role === 'user') {
                    // 检测是否是最后一条且为用户消息（悬挂状态）
                    const isLast = idx === messages.length - 1;
                    renderUserMessage(chatContainer, msg.content, msg.time, msg.files, isLast, msg.pair_id);
                } else {
                    renderAiMessage(chatContainer, msg);
                }
            });

            scrollToBottom(forceScroll);
        } else {
            // console.error('Failed to load conversation:', data.error);
            showNewChatUI();
        }
    } catch (e) {
        // console.error('Load messages error', e);
        showNewChatUI();
    }
}

// ==================== 渲染消息 ====================

// 渲染用户消息
function renderUserMessage(container, content, time, files = [], showRetry = false, pairId = null) {
    const filesHtml = files.length > 0 ?
        `<div class="mt-2 space-y-1">${files.map(file => `<div class="flex items-center text-xs text-gray-600"><i class="fa fa-file-o mr-1"></i><span>${escapeHtml(file.name)}</span></div>`).join('')}</div>` : '';

    const retryHtml = showRetry ? `
        <div class="retry-container mr-2 self-center">
            <button onclick="retryMessage(this)" class="text-red-600 hover:text-red-700 transition-colors" title="重试">
                <i class="fa fa-exclamation-circle text-xl"></i>
            </button>
        </div>` : '';

    const userHtml = `
  <div class="chat-message-wrapper justify-end user-message-wrapper" ${pairId ? `data-pair-id="${pairId}"` : ''}>
      ${retryHtml}
      <div class="flex flex-col items-end" style="max-width: 60%;">
          <div class="chat-bubble-user">
              ${escapeHtml(content).replace(/\n/g, '<br>')}
              ${filesHtml}
          </div>
          <div class="chat-time">${time}</div>
      </div>
      <div class="chat-avatar ml-2">
          <div class="w-full h-full bg-gray-100 flex items-center justify-center text-lg select-none" style="border-radius: 4px;">
            ${userAvatar}
          </div>
      </div>
  </div>`;
    container.insertAdjacentHTML('beforeend', userHtml);
}

// 渲染AI消息
function renderAiMessage(container, msg) {
    const content = msg.content;
    const time = msg.time;
    const pairId = msg.pair_id || '';
    const versions = msg.versions || [content];
    const activeIndex = msg.active_index !== undefined ? msg.active_index : 0;
    const showPagination = versions.length > 1;

    const aiHtml = `
  <div class="chat-message-wrapper justify-start assistant-message" data-pair-id="${pairId}">
      <div class="chat-avatar mr-2">
          <div class="w-full h-full overflow-hidden" style="border-radius: 4px;">
            ${aiAvatarSvg}
          </div>
      </div>
      <div class="flex flex-col items-start" style="max-width: 60%;">
          <div class="chat-bubble-ai">
              ${escapeHtml(content).replace(/\n/g, '<br>')}
          </div>
          <div class="flex items-center space-x-3 chat-time">
              <span>${time}</span>
              <button class="text-gray-400 hover:text-gray-600 transition-colors" title="复制" onclick="copyMessage(this)">
                <i class="fa fa-copy"></i>
              </button>
              <button class="text-gray-400 hover:text-gray-600 transition-colors regenerate-btn" title="重新回答" onclick="regenerateMessage(this)">
                <i class="fa fa-refresh"></i>
              </button>
              <div class="pagination-controls flex items-center space-x-1 ${showPagination ? '' : 'hidden'}">
                  <button onclick="switchMessageVersion(this, -1)" class="text-gray-400 hover:text-gray-600"><i class="fa fa-chevron-left text-xs"></i></button>
                  <span class="page-text text-xs text-gray-500">${activeIndex + 1}/${versions.length}</span>
                  <button onclick="switchMessageVersion(this, 1)" class="text-gray-400 hover:text-gray-600"><i class="fa fa-chevron-right text-xs"></i></button>
              </div>
          </div>
      </div>
  </div>`;
    container.insertAdjacentHTML('beforeend', aiHtml);
}

// ==================== 加载指示器 ====================

// 显示加载指示器（使用全局 aiAvatarSvg）
function showLoadingIndicator() {
    const container = document.getElementById('chat-container');
    const currentTime = getCurrentTime();
    const loadingHtml = `
  <div id="loading-indicator" class="chat-message-wrapper justify-start">
      <div class="chat-avatar mr-2">
          <div class="w-full h-full overflow-hidden" style="border-radius: 4px;">
            ${aiAvatarSvg}
          </div>
      </div>
      <div class="flex flex-col items-start" style="max-width: 60%;">
          <div class="chat-bubble-ai" style="display: flex; align-items: center; justify-content: center; min-height: 40px; padding: 10px 12px;">
            <div style="display: flex; align-items: center; gap: 8px;">
              <div style="width: 8px; height: 8px; border-radius: 50%; background-color: rgba(255, 255, 255, 0.95); animation: pulse 1.2s cubic-bezier(0.4, 0, 0.6, 1) infinite; animation-delay: 0s;"></div>
              <div style="width: 8px; height: 8px; border-radius: 50%; background-color: rgba(255, 255, 255, 0.95); animation: pulse 1.2s cubic-bezier(0.4, 0, 0.6, 1) infinite; animation-delay: 0.2s;"></div>
              <div style="width: 8px; height: 8px; border-radius: 50%; background-color: rgba(255, 255, 255, 0.95); animation: pulse 1.2s cubic-bezier(0.4, 0, 0.6, 1) infinite; animation-delay: 0.4s;"></div>
            </div>
          </div>
          <div class="flex items-center space-x-2 chat-time" style="visibility: visible;">
              <span>${currentTime}</span>
              <span class="loading-status-area flex items-center space-x-1 text-gray-400">
                  <i class="fa fa-spinner fa-spin"></i>
                  <span class="status-text">AI正在思考...</span>
              </span>
          </div>
      </div>
  </div>
  <style>
    @keyframes pulse {
      0%, 100% {
        transform: scale(0.8);
        opacity: 0.5;
      }
      50% {
        transform: scale(1.2);
        opacity: 1;
      }
    }
  </style>`;
    container.insertAdjacentHTML('beforeend', loadingHtml);
    scrollToBottom(true); // 显示加载状态时，通常是刚发消息，强制滚动
}

/**
 * 更新加载指示器中的文字状态
 */
function updateLoadingIndicatorStatus(text) {
    const indicator = document.getElementById('loading-indicator');
    if (indicator) {
        const statusText = indicator.querySelector('.status-text');
        if (statusText) {
            statusText.textContent = text;
        }
    }
}

// 移除加载指示器
function removeLoadingIndicator() {
    const indicator = document.getElementById('loading-indicator');
    if (indicator) {
        indicator.remove();
    }
}

// ==================== 发送消息 ====================

// 发送消息
async function sendMessage() {
    // 获取DOM元素
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const charCount = document.getElementById('char-count');
    const filePreviewArea = document.getElementById('file-preview-area');
    const fileUpload = document.getElementById('file-upload');

    const text = userInput.value.trim();
    if (!text && currentFiles.length === 0) return;

    // 立即隐藏欢迎消息（在任何操作之前）
    const welcomeMsg = document.getElementById('welcome-message');
    if (welcomeMsg) {
        welcomeMsg.classList.add('hidden');
        welcomeMsg.style.display = 'none';
    }

    if (!currentConversationId) {
        // 如果未选择对话，自动创建
        try {
            const res = await fetch('/api/cost-ai/conversations', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ title: text.substring(0, 50) || '新对话' })
            });
            const data = await res.json();
            if (data.success) {
                currentConversationId = data.conversation.id;
                // 更新 URL
                const shortId = currentConversationId.startsWith('conv_') ? currentConversationId.substring(5) : currentConversationId;
                window.history.pushState({ id: currentConversationId }, '', `/cost-ai/${shortId}`);
                renderConversationList(); // 刷新列表显示新对话
            } else {
                alert('创建对话失败: ' + (data.error || '未知错误'));
                return;
            }
        } catch (e) {
            // console.error('Auto-create conversation error:', e);

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
                alert('网络错误，无法创建对话');
            }
            return;
        }
    }

    const container = document.getElementById('chat-container');
    const currentTime = getCurrentTime();

    // 乐观 UI 更新用户消息
    renderUserMessage(container, text, currentTime, currentFiles);
    scrollToBottom(true); // 用户发送消息，必须强制滚动

    // 清除输入和文件
    userInput.value = '';
    userInput.style.height = 'auto';
    charCount.textContent = '0/2000';
    charCount.classList.add('opacity-0');
    filePreviewArea.innerHTML = '';
    filePreviewArea.classList.add('hidden');
    currentFiles = [];
    fileUpload.value = ''; // 清除文件输入

    // 处理时禁用输入
    userInput.disabled = true;
    sendBtn.disabled = true;

    showLoadingIndicator();

    const formData = new FormData();
    formData.append('message', text);
    formData.append('conversation_id', currentConversationId);
    currentFiles.forEach(file => {
        formData.append('files', file);
    });

    try {
        if (streamEnabled) {
            // ==================== 流式发送 ====================
            // 注意：保留三个点加载动画，直到收到第一个字符

            const response = await fetch('/api/cost-ai/chat/stream', {
                method: 'POST',
                body: formData
            });

            // console.log('流式响应状态:', response.status);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const reader = response.body.getReader();
            const decoder = new TextDecoder();
            let buffer = '';
            let streamBubble = null;  // 延迟创建气泡
            let hasReceivedFirstChunk = false;

            // console.log('开始读取流式数据...');
            while (true) {
                const { done, value } = await reader.read();
                if (done) {
                    // console.log('读取器(Reader)已完成');
                    break;
                }

                const chunkContent = decoder.decode(value, { stream: true });
                buffer += chunkContent;
                // console.log('收到原始Chunk:', chunkContent);

                // 按行处理SSE数据
                const lines = buffer.split('\n');
                buffer = lines.pop() || ''; // 保留未完成的行

                for (const line of lines) {
                    const trimmedLine = line.trim();
                    if (!trimmedLine) continue;

                    // console.log('正在处理行:', trimmedLine);
                    if (trimmedLine.startsWith('data: ')) {
                        const dataStr = trimmedLine.substring(6).trim();

                        // 检查结束标记
                        if (dataStr === '[DONE]') {
                            // console.log('收到[DONE]标记');
                            continue;
                        }

                        try {
                            const data = JSON.parse(dataStr);
                            // console.log('解析后的数据对象:', data);

                            // 检查并更新状态
                            if (data.status) {
                                // console.log('收到状态更新:', data.status);
                                updateLoadingIndicatorStatus(data.status);
                                continue;
                            }

                            // 追加文本到气泡
                            if (data.text) {
                                // 收到第一个字符时，移除加载动画并创建流式气泡
                                if (!hasReceivedFirstChunk) {
                                    // console.log('收到第一个文本字符，创建气泡...');
                                    removeLoadingIndicator();
                                    streamBubble = createStreamingAiBubble(container);
                                    hasReceivedFirstChunk = true;
                                }
                                appendToStreamingBubble(streamBubble, data.text);
                            }

                            // 检查是否完成
                            if (data.done) {
                                // console.log('数据标记为完成(done)');
                                // 如果还没收到任何文本但已标记完成，说明是一次性响应
                                // 需要先移除加载动画
                                if (!hasReceivedFirstChunk) {
                                    // console.log('标记完成但尚未收到文本，移除加载动画');
                                    removeLoadingIndicator();
                                }
                                // 只有创建！了气泡才需要finalize
                                if (hasReceivedFirstChunk) {
                                    // console.log('Finalizing 气泡');
                                    finalizeStreamingBubble(getCurrentTime(), data.pair_id, data.versions_count, data.active_index);
                                }
                            }

                            // 检查错误
                            if (data.error) {
                                // console.error('流式响应逻辑错误:', data.text);
                            }
                        } catch (parseErr) {
                            // console.error('SSE解析失败:', parseErr, '数据字符串:', dataStr);
                        }
                    }
                }
            }

            // 确保完成状态（仅当已创建气泡时）
            if (hasReceivedFirstChunk) {
                // 流式结束时 data 可能已经不可见，这里尝试用最后一批数据
                // 但通常 done 分块里有完整信息
            } else {
                // 如果没收到任何内容，移除加载动画
                removeLoadingIndicator();
            }

        } else {
            // ==================== 非流式发送（原有逻辑）====================
            const res = await fetch('/api/cost-ai/chat', {
                method: 'POST',
                body: formData
            });
            const data = await res.json();
            removeLoadingIndicator();
            if (data.success) {
                renderAiMessage(container, {
                    content: data.message,
                    time: getCurrentTime(),
                    pair_id: data.data ? data.data.pair_id : null
                });
            } else {
                alert('发送失败: ' + (data.error || '未知错误'));
            }
        }

        scrollToBottom(true); // 全部完成后，确保到达底部（可选，稳妥起见）
        // 刷新对话列表以更新预览/时间
        renderConversationList();

    } catch (err) {
        removeLoadingIndicator();
        // 移除可能存在的流式气泡
        const streamingMsg = document.getElementById('streaming-message');
        if (streamingMsg) streamingMsg.remove();

        // 在最后一条用户消息上显示重试按钮
        const userMessages = container.querySelectorAll('.chat-message-wrapper.justify-end');
        if (userMessages.length > 0) {
            const lastUserMsg = userMessages[userMessages.length - 1];
            if (!lastUserMsg.querySelector('.retry-container')) {
                const retryHtml = `
                    <div class="retry-container mr-2 self-center">
                        <button onclick="retryMessage(this)" class="text-red-600 hover:text-red-700 transition-colors" title="重试">
                            <i class="fa fa-exclamation-circle text-xl"></i>
                        </button>
                    </div>`;
                lastUserMsg.insertAdjacentHTML('afterbegin', retryHtml);
            }
        }

        // console.error('Send message error:', err);

        // 检测是否是页面刷新/卸载导致的错误
        const isNavigationError =
            err.name === 'AbortError' ||
            err.name === 'TypeError' && (
                err.message.includes('Failed to fetch') ||
                err.message.includes('NetworkError') ||
                err.message.includes('cancelled') ||
                err.message.includes('aborted')
            );

        // 只有在不是页面刷新/卸载导致的错误时才弹出提示
        if (!isNavigationError) {
            alert('网络错误');
        }
    } finally {
        userInput.disabled = false;
        sendBtn.disabled = false;
        userInput.focus();
    }
}

// ==================== 输入框事件监听器 ====================

// 设置消息输入相关的事件监听器
document.addEventListener('DOMContentLoaded', () => {
    const sendBtn = document.getElementById('send-btn');
    const userInput = document.getElementById('user-input');
    const fileUpload = document.getElementById('file-upload');
    const charCount = document.getElementById('char-count');
    const filePreviewArea = document.getElementById('file-preview-area');

    // 自动调整文本框高度和字符计数
    if (userInput) {
        userInput.addEventListener('input', function () {
            this.style.height = 'auto';
            this.style.height = this.scrollHeight + 'px';

            const length = this.value.length;
            charCount.textContent = `${length}/2000`;

            if (length > 2000) {
                charCount.classList.add('text-red-500');
                this.value = this.value.substring(0, 2000);
            } else {
                charCount.classList.remove('text-red-500');
            }

            charCount.classList.toggle('visible', length > 0);
            sendBtn.disabled = length === 0;
        });
    }

    // 发送按钮点击
    if (sendBtn) {
        sendBtn.addEventListener('click', sendMessage);
    }

    // 回车发送
    if (userInput) {
        userInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });
    }
});

// ==================== 重新回答与版本切换 ====================

// 重新回答
async function regenerateMessage(btn) {
    const wrapper = btn.closest('.chat-message-wrapper');
    const pairId = wrapper.getAttribute('data-pair-id');
    const bubble = wrapper.querySelector('.chat-bubble-ai');
    const timeEl = wrapper.querySelector('.chat-time');
    if (!pairId || !currentConversationId || !bubble) return;

    // 禁用按钮防抖
    btn.disabled = true;
    const originalIcon = btn.innerHTML;
    btn.innerHTML = '<i class="fa fa-spinner fa-spin"></i>';

    // 原地更新准备：清空气泡，隐藏时间栏，添加光标
    bubble.innerHTML = '<span class="streaming-cursor"></span>';
    if (timeEl) timeEl.style.visibility = 'hidden';

    const formData = new FormData();
    formData.append('conversation_id', currentConversationId);
    formData.append('regenerate_pair_id', pairId);

    try {
        if (streamEnabled) {
            // 流式重新回答 (原地更新)
            await performChatRequest(formData, wrapper, bubble);
        } else {
            // 非流式重新回答
            const res = await fetch('/api/cost-ai/chat', {
                method: 'POST',
                body: formData
            });
            const data = await res.json();
            if (data.success) {
                // 原地填充内容并恢复 UI
                bubble.innerHTML = escapeHtml(data.message).replace(/\n/g, '<br>');
                finalizeStreamingBubble(getCurrentTime(), pairId, data.versions_count || 1, data.active_index || 0, wrapper);
            } else {
                alert('重试失败: ' + data.error);
                // 恢复 UI 状态（此处可优化：重新加载对话以恢复旧内容）
                loadConversationMessages(currentConversationId);
            }
        }
    } catch (e) {
        console.error('Regenerate error:', e);
        loadConversationMessages(currentConversationId);
    } finally {
        btn.disabled = false;
        btn.innerHTML = originalIcon;
    }
}

// 封装通用的聊天请求逻辑
async function performChatRequest(formData, targetWrapper = null, targetBubble = null) {
    const container = document.getElementById('chat-container');

    try {
        const response = await fetch('/api/cost-ai/chat/stream', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) throw new Error(`HTTP ${response.status}`);

        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';
        let streamBubble = targetBubble; // 如果是原地更新，则使用传入的气泡
        let hasReceivedFirstChunk = false;

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            const chunkContent = decoder.decode(value, { stream: true });
            buffer += chunkContent;
            const lines = buffer.split('\n');
            buffer = lines.pop() || '';

            for (const line of lines) {
                const trimmedLine = line.trim();
                if (!trimmedLine.startsWith('data: ')) continue;
                const dataStr = trimmedLine.substring(6).trim();
                if (dataStr === '[DONE]') continue;

                try {
                    const data = JSON.parse(dataStr);
                    if (data.status) {
                        updateLoadingIndicatorStatus(data.status);
                        continue;
                    }
                    if (data.text) {
                        if (!hasReceivedFirstChunk) {
                            // 如果不是原地更新，才需要移除全局加载动画
                            if (!targetBubble) {
                                removeLoadingIndicator();
                            }
                            // 如果不是原地更新，则创建新气泡
                            if (!streamBubble) {
                                streamBubble = createStreamingAiBubble(container);
                            }
                            hasReceivedFirstChunk = true;
                        }
                        appendToStreamingBubble(streamBubble, data.text);
                    }
                    if (data.done) {
                        // 如果没有收到任何文本，但标记完成，需要移除全局加载动画
                        if (!hasReceivedFirstChunk && !targetBubble) removeLoadingIndicator();
                        // 如果有气泡（无论是原地还是新创建的），完成它
                        const wrapperForFinalize = targetWrapper || document.getElementById('streaming-message');
                        if (wrapperForFinalize || streamBubble) {
                            finalizeStreamingBubble(getCurrentTime(), data.pair_id, data.versions_count, data.active_index, targetWrapper);
                        }
                    }
                } catch (e) { }
            }
        }
        if (typeof renderConversationList === 'function') {
            renderConversationList();
        }
    } catch (err) {
        removeLoadingIndicator();
        console.error('Chat request error:', err);
    }
}

// 切换版本
async function switchMessageVersion(btn, direction) {
    const wrapper = btn.closest('.chat-message-wrapper');
    const pairId = wrapper.getAttribute('data-pair-id');
    const pageText = wrapper.querySelector('.page-text');
    if (!pageText || !pairId || !currentConversationId) return;

    const parts = pageText.textContent.split('/');
    let currentIndex = parseInt(parts[0]) - 1;
    const total = parseInt(parts[1]);

    let newIndex = currentIndex + direction;
    if (newIndex < 0) newIndex = total - 1;
    if (newIndex >= total) newIndex = 0;

    if (newIndex === currentIndex) return;

    try {
        const res = await fetch(`/api/cost-ai/conversations/${currentConversationId}/messages/${pairId}/switch`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ index: newIndex })
        });
        const data = await res.json();
        if (data.success) {
            await loadConversationMessages(currentConversationId, false);
        }
    } catch (e) {
        console.error('Switch version error:', e);
    }
}
// 重试发送消息
async function retryMessage(btn) {
    const wrapper = btn.closest('.chat-message-wrapper');
    const pairId = wrapper.getAttribute('data-pair-id');
    const bubble = wrapper.querySelector('.chat-bubble-user');
    if (!bubble || !currentConversationId) return;

    // 获取消息文本（排除文件列表部分）
    const text = bubble.innerText.split('\n')[0].trim();

    // 移除当前的重试图标，显示加载状态
    btn.innerHTML = '<i class="fa fa-spinner fa-spin text-xl text-gray-400"></i>';
    btn.disabled = true;

    const formData = new FormData();
    formData.append('message', text);
    formData.append('conversation_id', currentConversationId);
    if (pairId) {
        formData.append('regenerate_pair_id', pairId);
    }

    try {
        // 先手动显示全局加载动画，模拟正在处理
        showLoadingIndicator();
        await performChatRequest(formData);

        // 发送成功后，移除该消息的重试容器（因为页面会刷新或局部更新）
        wrapper.querySelector('.retry-container')?.remove();
    } catch (e) {
        console.error('Retry failed:', e);
        btn.innerHTML = '<i class="fa fa-exclamation-circle text-xl"></i>';
        btn.disabled = false;
    } finally {
        removeLoadingIndicator();
    }
}
