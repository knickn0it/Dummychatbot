document.getElementById("send-button").addEventListener("click", async function () {
    const userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    // Display user message in the chat box
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div><strong>You:</strong> ${userInput}</div>`;

    // Send message to the Flask backend
    const response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userInput }),
    });

    const data = await response.json();
    const chatbotResponse = data.response;

    // Display chatbot's response
    chatBox.innerHTML += `<div><strong>Chatbot:</strong> ${chatbotResponse}</div>`;

    // Clear the input field
    document.getElementById("user-input").value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
});
