
function playAudio(file){
    const audio = document.getElementById('audioPlayer');
    audio.src = file;
    audio.load();
    audio.play();
}
