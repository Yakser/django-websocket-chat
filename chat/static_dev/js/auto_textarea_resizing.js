const autoTextareaResizing = () => {
    const textarea = document.getElementById('chat-message-input');
    textarea.style.height = textarea.scrollHeight + 'px';
    textarea.style.overflowY = 'hidden';

    textarea.addEventListener('input', (event) => {
        textarea.style.height = 'auto';
        textarea.style.height = textarea.scrollHeight + 'px';
    })
}

autoTextareaResizing();