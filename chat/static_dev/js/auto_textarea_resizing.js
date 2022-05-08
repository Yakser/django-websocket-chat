const autoTextareaResizing = () => {
    const textarea = document.getElementById('chat-message-input');
    textarea.addEventListener('input', (event) => {
        textarea.style.height = "5px";
        textarea.style.height = (textarea.scrollHeight) + "px";
    })
}

autoTextareaResizing();