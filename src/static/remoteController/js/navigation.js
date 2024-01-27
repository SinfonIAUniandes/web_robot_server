var speedSlider = document.getElementById("speed");
var displaySpeed = document.getElementById("showSp");
var speed = speedSlider.value;
var textbox = document.getElementById("palabras");
var izquierdo = document.getElementById("izquierdo");
var derecho = document.getElementById("derecho");
var arriba = document.getElementById("arriba");
var abajo = document.getElementById("abajo");
var angle = 0.45;
var left = 0.75;
var right = -0.75;
var up = -0.5;
var down = 0.5;
displaySpeed.innerHTML = "Velocidad: "+speed/100;

speedSlider.oninput = function(){
    displaySpeed.innerHTML = "Velocidad: "+this.value/100;
}
window.addEventListener("keydown", checkKeyPressed, false);
function checkKeyPressed(evt) {
    speed = speedSlider.value;
    if (document.activeElement!=textbox)
    {
        //a
        if (evt.keyCode == "65") {
            peticion = new XMLHttpRequest();
            peticion.open("GET","move/?direction=left&speed="+speed);
            peticion.send();
        }
        //d
        if (evt.keyCode == "68") {
            peticion = new XMLHttpRequest();
            peticion.open("GET","move/?direction=right&speed="+speed);
            peticion.send();
        }
        //w
        if (evt.keyCode == "87") {
            peticion = new XMLHttpRequest();
            peticion.open("GET","move/?direction=up&speed="+speed);
            peticion.send();
        }
        //s
        if (evt.keyCode == "83") {
            peticion = new XMLHttpRequest();
            peticion.open("GET","move/?direction=down&speed="+speed);
            peticion.send();            
        }
        //e
        if (evt.keyCode == "69") {
            peticion = new XMLHttpRequest();
            peticion.open("GET","move/?direction=rotateR&speed="+speed);
            peticion.send();            
        }
        //q
        if (evt.keyCode == "81") {
            peticion = new XMLHttpRequest();
            peticion.open("GET","move/?direction=rotateL&speed="+speed);
            peticion.send();            
        }

        //MOVE ROBOT HEAD
        //j 0, 1.5*angle
        if (evt.keyCode == "74") {
            peticion = new XMLHttpRequest();
            peticion.open("GET","moveHead/?angle0="+0+"&angle1="+(left*angle));
            peticion.send();
            right = 0;
            up = -0.5;
            down = 0.5;
            if(left==0)
            {
                left=0.75;
            }
            else
            {
                left = 1.5;
            }
        }
        //l 0,-1.5*angle
        if (evt.keyCode == "76") {
            peticion = new XMLHttpRequest();
            peticion.open("GET","moveHead/?angle0="+0+"&angle1="+(right*angle));
            peticion.send();
            left = 0;
            up = -0.5;
            down = 0.5;
            if(right==0)
            {
                right=-0.75;
            }
            else
            {
                right = -1.5;
            }
        }
        //i -1.0*angle,0
        if (evt.keyCode == "73") {
            peticion = new XMLHttpRequest();
            peticion.open("GET","moveHead/?angle0="+(up*angle)+"&angle1="+0);
            peticion.send();
            left = 0.75;
            right = -0.75;
            down = 0;
            if(up==0)
            {
                up=-0.5;
            }
            else
            {
                up = -1.0;
            }

        }
        //k 1.0*angle,0
        if (evt.keyCode == "75") {
            peticion = new XMLHttpRequest();
            peticion.open("GET","moveHead/?angle0="+(down*angle)+"&angle1="+0);
            peticion.send();
            left = 0.75;
            right = -0.75;
            up = 0;
            if(down==0)
            {
                down=0.5;
            }
            else
            {
                down = 1.0;
            }
        }
    }
}
var executer;
function move(direction){
    speed = speedSlider.value;
    executer = setInterval(function() {
        peticion = new XMLHttpRequest();
        peticion.open("GET","move/?direction="+direction+"&speed="+speed);
        peticion.send();    
    }, 500);        
}
function stop(){
    clearInterval(executer);
}
function tapMove(direction){
    peticion = new XMLHttpRequest();
    peticion.open("GET","move/?direction="+direction+"&speed="+speed);
    peticion.send();
}

let controllerIndex = null;

window.addEventListener("gamepadconnected", (event) => {
  controllerIndex = 0;
  console.log("connected");
});

window.addEventListener("gamepaddisconnected", (event) => {
  controllerIndex = null;
  console.log("disconnected");
});

function handleSticks(axes)
{
    horizontalAxisL = axes[0];
    verticalAxisL = axes[1];
    horizontalAxisR = axes[2];
    verticalAxisR = axes[3];
    const stickHorizontalL = horizontalAxisL * speed/100;
    const stickVerticalL = verticalAxisL * speed/100;
    const stickHorizontalR = horizontalAxisR;
    const stickVerticalR = verticalAxisR;
    if (Math.abs(0-stickHorizontalL)>0.1 || Math.abs(0-stickVerticalL)>0.1)
    {
        peticion = new XMLHttpRequest();
        peticion.open("GET","joyStick/?verticalAxis="+stickVerticalL+"&horizontalAxis="+stickHorizontalL);
        peticion.send();
    }
    if (Math.abs(0-stickHorizontalR)>0.1 || Math.abs(0-stickVerticalR)>0.1)
    {
        peticion = new XMLHttpRequest();
        peticion.open("GET","joyStick/?verticalAxis="+stickVerticalL+"&horizontalAxis="+stickHorizontalL);
        peticion.send();
    }
}

setInterval(gameLoop,50);

function gameLoop()
{
    if (controllerIndex !== null)
    {
        const gamepad = navigator.getGamepads()[controllerIndex];
        handleSticks(gamepad.axes);
    }
}