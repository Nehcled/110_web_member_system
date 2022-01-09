// Input set
const utterances = [
    "怎麼獲得隱藏獎勵?",
    "會員等級如何提升?",
];

// Output set
const answers = [
    "提升您的會員等級!",
    "每天登入簽到!",
];

// Random for any other user input, if not any answer fit in
const alternatives = ["試試別的選項!", "我不知道~", "老兄，不要點上面沒有的!"];

function compare(answersArray, userInput) {
    let reply;
    reply = answersArray[parseInt(userInput) - 1];
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


    botDiv.appendChild(botText);
    messagesContainer.appendChild(botDiv);

    messagesContainer.scrollTop =
        messagesContainer.scrollHeight - messagesContainer.clientHeight;

    setTimeout(() => {
        botText.innerText = `${product}`;
    }, 1000);
}
function output(input) {
    let product;
    let text = input;

    if (compare(answers, text)) {
        // Search for exact match in triggers
        product = compare(answers, text);
    }
    else if (text === ""){
        product = "你還沒輸入，歸剛欸"
    }
    else {
        product = alternatives[Math.floor(Math.random() * alternatives.length)];
    }

    addChatEntry(input, product);
}

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


function blurButton(elementId){
    document.getElementById(elementId).blur();
}

function openOrClose(){
    $("#messages").slideToggle(300);
    $("#typing-area").slideToggle(300);
}