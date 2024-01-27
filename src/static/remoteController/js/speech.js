var volumeSlider = document.getElementById("volume");
var displayVolume = document.getElementById("showVo");
var volumen = volumeSlider.value;
var textbox = document.getElementById("palabras");
var muteado =  false;
displayVolume.innerHTML = "Volumen: "+volumen;

volumeSlider.oninput = function(){
    displayVolume.innerHTML = "Volumen: "+this.value;
}
function speak(){
    lenguaje = document.getElementById("lenguaje").value;
    palabras = textbox.value;
    peticion = new XMLHttpRequest();
    peticion.open("GET","speak/?language="+lenguaje+"&words="+palabras);
    peticion.send();
}
function setVolume(){
    volume = document.getElementById("volume").value;
    peticion = new XMLHttpRequest();
    peticion.open("GET","setVolume/?volume="+volume);
    peticion.send();
}

function mute()
{
    muteado = !muteado;
}


contador2 = 0;
let xmlhttp = new XMLHttpRequest();
url = "getAudio/"
enableAudio();
audioEnabled = true;
const handler = new window.AudioContext();
function updateProgress (oEvent) {
    if (contador2>=15)
    {
        audioData = oEvent.currentTarget.response.split(",").splice(-20650);
        audioData.pop();
        playAudio(audioData);
        contador2=0;
    }
    contador2+=1;
}
function playAudio(data)
{
    const audioBuffer1 = handler.createBuffer(1,data.length,16000);
    const channel = audioBuffer1.getChannelData(0);
    for(let i=0;i<data.length;i++)
    {
        channel[i]=data[i]/32768.0;
    }
    const source = handler.createBufferSource();
    source.buffer = audioBuffer1;
    source.connect(handler.destination);
    source.start();
}
function enableAudio()
{
    xmlhttp.addEventListener('progress', updateProgress, false);
    xmlhttp.open("get", url, true);
    xmlhttp.send();
    console.log("transmision iniciada");
}
function disableAudio()
{
    xmlhttp.removeEventListener('progress',updateProgress);
    xmlhttp.open("get", url, true);
    xmlhttp.send();
    console.log("transmision detenida");
}
audioButton = document.getElementById("audio")
function changeAudio()
{
    if (!audioEnabled)
    {
        enableAudio();
        audioEnabled=!audioEnabled;
        audioButton.innerHTML = "Detener Transmision de Audio"
    }
    else
    {
        disableAudio();
        audioEnabled=!audioEnabled;
        audioButton.innerHTML = "Iniciar Transmision de Audio"
    }
}