const roomName = JSON.parse(document.getElementById('group-name').textContent);
const chatSocket = new WebSocket(`ws://${window.location.host}/ws/chat/${roomName}/`);


chatSocket.onmessage = function (e) {
    moment.locale('ru')
    const data = JSON.parse(e.data);
    if (data.message.trim().length > 0) {
        const chatLog = document.querySelector('#chat-log');
        chatLog.insertAdjacentHTML('beforeend', `<div class='message'><span class='message__text'>${data.message}</span>  <span class='message__time'>${moment().fromNow()}</span></div>`);
        chatLog.scrollTop = chatLog.scrollHeight;
    }
};

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly', e);
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function (e) {
    if (e.keyCode === 13) { // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function (e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};