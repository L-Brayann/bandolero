var audio = document.getElementById("musica");

function tocarMusica() {
    if (audio.paused) {
        audio.play();
    } else {
        audio.pause();
    }
}

function proximaMusica() {
    // Substitua "caminho_da_proxima_musica.mp3" pelo caminho real da próxima música
    audio.src = "assets\music\Matuê   Conexões de Máfia feat Rich the Ki[1].mp3";
    audio.play();
}
