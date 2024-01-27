function display(){
    url = document.getElementById("urlImagen").value;
    peticion = new XMLHttpRequest();
    peticion.open("GET","show_img/?url="+url);
    peticion.send();
}

function displayWeb(){
    url = document.getElementById("urlWeb").value;
    peticion = new XMLHttpRequest();
    peticion.open("GET","show_web/?url="+url);
    peticion.send();
}

function dropHandler(ev) {
    console.log("File(s) dropped");

    // Prevent default behavior (Prevent file from being opened)
    ev.preventDefault();

    if (ev.dataTransfer.items) {
        // Use DataTransferItemList interface to access the file(s)
        [...ev.dataTransfer.items].forEach((item, i) => {
        // If dropped items aren't files, reject them
        if (item.kind === "file") {
            const file = item.getAsFile();
            console.log(`… file[${i}].name = ${file.name}`);
            var reader  = new FileReader();
            // it's onload event and you forgot (parameters)
            var image = document.getElementById("preview");
            reader.onload = function(e)  {
                // the result image data
                image.src = e.target.result;
                formData = new FormData();
                formData.append("imagen",file);
                request = new XMLHttpRequest();
                request.open("POST","save_img/?");
                request.send(formData);
            }
             // you have to declare the file loading
            reader.readAsDataURL(file);
        }
        });
    } 
    else {
        // Use DataTransfer interface to access the file(s)
        [...ev.dataTransfer.files].forEach((file, i) => {
        console.log(`… file[${i}].name = ${file.name}`);
        });
    }
}

function dragOverHandler(ev) {
    console.log("File(s) in drop zone");

    // Prevent default behavior (Prevent file from being opened)
    ev.preventDefault();
}

function display2() {

    var file = document.getElementById('imagenT').files[0];
    var reader  = new FileReader();
    // it's onload event and you forgot (parameters)
    reader.onload = function(e)  {
        var image = document.getElementById("preview");
        // the result image data
        image.src = e.target.result;
        formData = new FormData();
        formData.append("imagen",file);
        request = new XMLHttpRequest();
        request.open("POST","save_img/?");
        request.send(formData);

    }
    // you have to declare the file loading
    reader.readAsDataURL(file);
}

function setLeds(){
    var colorH = document.getElementById("leds").value;
    red = parseInt(colorH.substring(1,3),16);
    green = parseInt(colorH.substring(3,5),16);
    blue = parseInt(colorH.substring(5,7),16);
    request = new XMLHttpRequest();
    request.open("GET","setLeds/?"+"red="+red+"&green="+green+"&blue="+blue);
    request.send();
}

getBattery();

setInterval(getBattery,60000);

function getBattery()
{
    peticion = new XMLHttpRequest();
    peticion.open("GET","getBattery/?");
    peticion.onreadystatechange = () => {
    if (peticion.readyState === 4) {
        var response = peticion.response;
        bateria = document.getElementById("battery");
        bateria.innerHTML = "Bateria: "+response+"%";
    }};
    peticion.send();
}
function delImgs()
{
    peticion = new XMLHttpRequest();
    peticion.open("GET","delImgs/?");
    peticion.send();        
}