const restoreScrollPos = () => {
    const chatsList = document.querySelector('.chats-list');

    document.addEventListener("DOMContentLoaded", function (event) {
        const scrollpos = localStorage.getItem('chatsScrollpos');
        if (scrollpos) chatsList.scrollTo(0, scrollpos);
    });

    window.onbeforeunload = function (e) {
        localStorage.setItem('chatsScrollpos', chatsList.scrollTop);
    }
}

restoreScrollPos();