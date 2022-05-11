const restoreMessagesScrollPos = () => {
    const chat = document.getElementById('chat-log');

    document.addEventListener("DOMContentLoaded", function (event) {
        const scrollpos = localStorage.getItem('chatScrollpos');
        if (scrollpos) chat.scrollTo(0, scrollpos);
    });

    window.onbeforeunload = function (e) {
        if (chat) {
            let pos = chat.scrollTop;
            if (pos == 0) {
                pos = 1;
            }
            localStorage.setItem('chatScrollpos', pos);
        }
        
    }
}

restoreMessagesScrollPos();