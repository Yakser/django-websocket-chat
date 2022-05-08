const autoTextareaResizing = () => {
    const textarea = document.getElementById('chat-message-input');
    const borderWidth = textarea.style.borderWidth;

    textarea.style.height = textarea.scrollHeight + 2 * borderWidth + 'px';
    textarea.style.overflowY = 'hidden';

    textarea.addEventListener('input', (event) => {
        textarea.style.height = 'auto';
        textarea.style.height = textarea.scrollHeight + 2 * borderWidth + 'px';
    })
}

autoTextareaResizing();