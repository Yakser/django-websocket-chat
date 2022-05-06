const connectionType= JSON.parse(document.getElementById('connection_type').textContent);
const connectionName = JSON.parse(document.getElementById('connection_name').textContent);

const chatSocket = new WebSocket(`ws://${window.location.host}/ws/chat/${connectionType}_${connectionName}/`);

const chatLog = document.querySelector('#chat-log');
chatLog.scrollTop = chatLog.scrollHeight;


moment.locale('ru');

chatSocket.onmessage = function (event) {
    const { username, message } = JSON.parse(event.data);
    const cleanedMessage = cleanMessage(message);

    if (validateMessage(message)) {
        const messageMarkup = `
        <div class='message'>
            <span class='message__author'>${username || 'Анонимный пользователь'}</span>
            <p class='message__text'>${cleanedMessage}</p>
            <span class='message__time'>${moment().format('h:mm:ss, MMMM Do')}</span>
        </div>`
        
        chatLog.insertAdjacentHTML('beforeend', messageMarkup);
        chatLog.scrollTop = chatLog.scrollHeight;
    }
};

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
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
    const message = cleanMessage(messageInputDom.value);
    if (validateMessage(message)) {
        try {
            chatSocket.send(JSON.stringify({
                'message': message,
            }));
            messageInputDom.value = '';
        } catch (e) {
            consol.error(e);
        }
    }
};


const cleanMessage = (message) => {
    return message.trim();
}

const validateMessage = (message) => {
    return message.length > 0;
}