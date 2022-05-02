const connectionType= JSON.parse(document.getElementById('connection_type').textContent);
const connectionName = JSON.parse(document.getElementById('connection_name').textContent);

const chatSocket = new WebSocket(`ws://${window.location.host}/ws/chat/${connectionType}_${connectionName}/`);

moment.locale('ru');

chatSocket.onmessage = function (e) {
    const { username, message } = JSON.parse(e.data);
    
    if (message.trim().length > 0) {
        const chatLog = document.querySelector('#chat-log');

        const messageMarkup = `
        <div class='message'>
            <span class='message__author'>${username || 'Анонимный пользователь'}</span>
            <p class='message__text'>${message}</p>
            <span class='message__time'>${moment().fromNow()}</span>
        </div>`

        chatLog.insertAdjacentHTML('beforeend', messageMarkup);
        chatLog.scrollTop = chatLog.scrollHeight;
    }
};

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly', e);
    alert('Произошла ошибка! Сервер недоступен.')
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
    const username = JSON.parse(document.getElementById('username').textContent);
    try {
        chatSocket.send(JSON.stringify({
            'message': message,
            'username': username
        }));
        messageInputDom.value = '';
    } catch (e) {
        consol.error(e);
    }
    
};