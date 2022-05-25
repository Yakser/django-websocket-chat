const pageReloadListener = () => {
    const chat = document.getElementById('chat-log');
    const chatsList = document.querySelector('.chats-list');

    document.addEventListener("DOMContentLoaded", function (event) {
        let scrollpos = localStorage.getItem('chatScrollpos');
        if (scrollpos) chat.scrollTo(0, scrollpos);

        scrollpos = localStorage.getItem('chatsScrollpos');
        if (scrollpos) chatsList.scrollTo(0, scrollpos);
    });

    window.onbeforeunload = function (e) {
        if (chat) {
            let pos = chat.scrollTop;
            if (pos == 0) {
                pos = 1;
            }
            localStorage.setItem('chatScrollpos', pos);
        }
        if (chatsList) localStorage.setItem('chatsScrollpos', chatsList.scrollTop);
    }
}

pageReloadListener();