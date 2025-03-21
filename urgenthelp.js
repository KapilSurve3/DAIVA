const signalingServer = new WebSocket("ws://acoustic-mercurial-mangosteen.glitch.me");

const chat = document.getElementById("confessions");
const messageInput = document.getElementById("chartcode");
const sendButton = document.getElementById("helpbtn");


signalingServer.onopen = () => {
    console.log("Connected to signaling server!");
    
};

signalingServer.onmessage = (event) => {
    const message = event.data;
    console.log("Received from server:", message);

    // Append the received message to the chat window
    const messageElement = document.createElement('div');
    messageElement.classList.add('chat-message', "help-message");
    messageElement.innerText = message;
    chat.appendChild(messageElement);
};

signalingServer.onerror = (error) => {
    console.log("WebSocket Error:", error);
};

signalingServer.onclose = () => {
    console.log("Connection closed.");
};

// Send message when button is clicked
sendButton.addEventListener("click", () => {
    const message = messageInput.value;
    if (message.trim()) {
        signalingServer.send(message);
        messageInput.value = ""; // Clear input field

        // Append the sent message to the chat window
        const sentMessageElement = document.createElement("div");
        sentMessageElement.classList.add('chat-message', "help-message");
        sentMessageElement.innerText =  message;
        chat.appendChild(sentMessageElement);
    }
});

// Allow pressing Enter key to send the message
messageInput.addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
        sendButton.click();
    }
});