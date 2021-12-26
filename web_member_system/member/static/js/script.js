// Input set
const utterances = [
    ["第一個選項"],
    ["第二個選項"],
    ["第三個選項"],
    ["第四個選項"],
];

// Output set
const answers = [
    ["第一個回答"],
    ["第二個回答"],
    ["第三個回答"],
    ["第四個回答"],
];

// Random for any other user input, if not any answer fit in
const alternatives = ["請再試一次", "我不知道~"];

document.addEventListener("DOMContentLoaded", () => {
    const messagesContainer = document.getElementById("messages");
    let botDiv = document.createElement("div");
    let botText = document.createElement("p");

    botDiv.id = "bot";
    botDiv.className = "bot response";
    botText.innerHTML += "輸入選項以讓我為您服務 " + "<br>";
    for (let i = 0; i < utterances.length; i++) {
        botText.innerHTML += "<br>";
        botText.innerHTML += (i + 1) + utterances[i];
    }
    botDiv.appendChild(botText);
    messagesContainer.appendChild(botDiv);
    // console.log(botText);

    //debug information
    document.querySelector("#input").addEventListener("keydown", function(e) {
        if (e.code === "Enter") {
            console.log("You pressed the enter button!");
        }
    });
    const inputField = document.getElementById("input");

    //control the send button
    document.getElementById("reply").addEventListener("click", function() {
        let input = inputField.value;
        inputField.value = "";
        output(input);
    });

    //if detect user press enter, send the messages
    inputField.addEventListener("keydown", function(e) {
        if (e.code === "Enter") {
            let input = inputField.value;
            inputField.value = "";
            output(input);
        }
    });
});

function output(input) {
    let product;
    let text = input;

    if (compare(answers, text)) {
        // Search for exact match in triggers
        product = compare(answers, text);
    } else {
        product = alternatives[Math.floor(Math.random() * alternatives.length)];
    }

    addChatEntry(input, product);
}

function compare(answersArray, userInput) {
    let reply;
    reply = answersArray[parseInt(userInput) - 1];
    console.log(reply);

    return reply;
}

function addChatEntry(input, product) {
    const messagesContainer = document.getElementById("messages");
    let userDiv = document.createElement("div");
    userDiv.id = "user";
    userDiv.className = "user response";
    userDiv.className = "item";
    userDiv.innerHTML = `<p>${input}</p>`;
    messagesContainer.appendChild(userDiv);

    let botDiv = document.createElement("div");
    let botText = document.createElement("p");

    botDiv.id = "bot";
    botDiv.className = "bot response";
    botDiv.className = "msg";

    botText.innerText = "輸入中...";
    botDiv.className = "msg";
    console.log(botText);

    botDiv.appendChild(botText);
    messagesContainer.appendChild(botDiv);

    messagesContainer.scrollTop =
        messagesContainer.scrollHeight - messagesContainer.clientHeight;

    setTimeout(() => {
        botText.innerText = `${product}`;
    }, 2000);
}