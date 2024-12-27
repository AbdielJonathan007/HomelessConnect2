// Code For the hamburger menu

function toggleMenu() {
    const menu = document.querySelector(".mobile-menu");  // The mobile menu
    const icon = document.querySelector(".hamburger-icon"); // The hamburger icon

    menu.classList.toggle("open");  // Toggle the 'open' class on the mobile menu
    icon.classList.toggle("open");  // Optional: Change hamburger icon when menu is opened
}
document.getElementById("open-chat-btn").addEventListener("click", function() {
    document.getElementById("chat-window").style.display = "block";
});

document.getElementById("close-chat-btn").addEventListener("click", function() {
    document.getElementById("chat-window").style.display = "none";
});



// Handle form submission and chat interaction
document.getElementById("chat-form").addEventListener("submit", async function(e) {
    e.preventDefault();
    const query = document.getElementById("query").value.trim();
    if (!query) return; // Do nothing if the input is empty

    // Display the user's message in the chat window
    const userMessageDiv = document.createElement("div");
    userMessageDiv.classList.add("chat-message", "user-message");
    userMessageDiv.innerText = query;
    document.getElementById("chat-messages").appendChild(userMessageDiv);

    // Scroll to the bottom of the chat
    document.getElementById("chat-messages").scrollTop = document.getElementById("chat-messages").scrollHeight;

    // Send the message to the backend and get the response
    const response = await fetch(`/chatbot/chat/?question=${encodeURIComponent(query)}`);
    const data = await response.json();

    // Display the chatbot's response in the chat window
    const botMessageDiv = document.createElement("div");
    botMessageDiv.classList.add("chat-message", "bot-message");
    botMessageDiv.innerText = data.response || "Sorry, I couldn't find an answer.";
    document.getElementById("chat-messages").appendChild(botMessageDiv);

    // Scroll to the bottom of the chat after the bot's message
    document.getElementById("chat-messages").scrollTop = document.getElementById("chat-messages").scrollHeight;

    // Clear the input field
    document.getElementById("query").value = "";
});
