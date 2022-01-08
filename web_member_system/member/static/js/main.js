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
