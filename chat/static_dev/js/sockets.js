moment.locale('ru');

const connectionType= JSON.parse(document.getElementById('connection_type').textContent);
const connectionName = JSON.parse(document.getElementById('connection_name').textContent);

const chatSocket = new WebSocket(`ws://${window.location.host}/ws/chat/${connectionType}_${connectionName}/`);

const chatLog = document.querySelector('#chat-log');
chatLog.scrollTop = chatLog.scrollHeight;

const chatInput = document.querySelector('#chat-message-input');
chatInput.focus();

const chatSubmit = document.querySelector('#chat-message-submit');


chatSocket.onmessage = function (event) {
    const { username, message } = JSON.parse(event.data);
    const cleanedMessage = cleanMessage(message);

    const currentUsername = document.querySelector('.user__username').textContent.trim();

    if (validateMessage(message)) {
        let messageClassRow = `<div class='message'>`

        if (currentUsername === username) {
            messageClassRow = `<div class='message current-user-message'>`
        }
        
        const messageMarkup = `
        ${messageClassRow}
            <span class='message__author'>${username || 'Анонимный пользователь'}</span>
            <p class='message__text'>${cleanedMessage}</p>
            <span class='message__time'>${moment().format('LT')}</span>
        </div>`
        
        chatLog.insertAdjacentHTML('beforeend', messageMarkup);
        chatLog.scrollTop = chatLog.scrollHeight;
    }
};

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
    // alert('Произошла ошибка! Сервер недоступен.')
};


chatInput.onkeydown = function (e) {
    if (e.keyCode === 13) { // enter, return
        e.preventDefault();

        chatInput.style.height = 'auto';
        chatSubmit.click();
    }
};

chatSubmit.onclick = function (event) {
    const message = cleanMessage(chatInput.value);
    if (validateMessage(message)) {
        try {
            chatSocket.send(JSON.stringify({
                'message': message,
            }));
            chatInput.value = '';
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