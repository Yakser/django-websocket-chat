const restoreChatsScrollPos = () => {
    const chatsList = document.querySelector('.chats-list');

    document.addEventListener("DOMContentLoaded", function (event) {
        let scrollpos = localStorage.getItem('chatsScrollpos');
        if (scrollpos) chatsList.scrollTo(0, scrollpos);
    });

    window.onbeforeunload = function (e) {
        if (chatsList) localStorage.setItem('chatsScrollpos', chatsList.scrollTop);
    }
}

restoreChatsScrollPos();