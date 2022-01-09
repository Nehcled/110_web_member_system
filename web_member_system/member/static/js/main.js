function goBackPage(){
    window.history.go(-1);
}
function selectFile(){
    $("#id_profile_photo").click();
}
function showFileName(){
    let fileName = $("#file-name");
    let file = document.getElementById("id_profile_photo")
    fileName.text(file.files ? file.files[0].name : "");
}

function closeWindow(window){
    document.getElementById(window).classList.add("hidden");
}
function showCover(){
    document.getElementById("cover").classList.remove("hidden");
}
function removeCover(){
    document.getElementById("cover").classList.add("hidden");
}
function openCardWindow(){
    let window = document.getElementById("window-card");
    window.classList.remove("hidden");
    window.style.zIndex = 10;

    showCover();
    document.getElementById("cover").addEventListener(
        "click",
        function(){
            closeWindow("window-card");
        }
    )
    document.getElementById("close").addEventListener(
        "click",
        function(){
            removeCover();
        }
    )
}