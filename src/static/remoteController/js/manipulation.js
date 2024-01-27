var grupos = document.getElementById("group");
var agregados = [];
var categoriasA =[];
var agregadosC = [];
var nombresA =[];
var todo;


fetch('http://'+ip+':8000/media/animations.txt').then(res=> res.blob()).then(blob=>{
    let reader = new FileReader();
    reader.addEventListener('loadend', (e)=>{
        const text = e.srcElement.result;
        animaciones = text.split("\n");
        todo = animaciones;
        for(var num in animaciones)
        {
            partes=animaciones[num].split("/");
            grupo = partes[0];
            if(agregados.includes(grupo) || grupo=="")
            {}   
            else
            {
                opcion = new Option(grupo,grupo);
                agregados.push(grupo);
                grupos.add(opcion,undefined);
            }             
        }
    });
    reader.readAsText(blob)
});


function listarCategorias(){
    nombres = document.getElementById("aName");
    cargado=false;
    categorias = document.getElementById("aCat");
    grupo = document.getElementById("group").value;
    nombres.innerHTML="";
    opcion = new Option("Elegir un nombre","");
    nombres.add(opcion,undefined);
    categorias.innerHTML="";
    opcion = new Option("Elegir una categoria","");
    opcion.defaultSelected= true;
    categorias.add(opcion,undefined);
    categorias.disabled = false;
    for(var num in todo)
        {
            partes=todo[num].split("/");
            grupoT = partes[0];
            if(partes.length==3)
            {
                if(grupoT==grupo)
                {
                    categoria = partes[1];
                    if(agregadosC.includes(categoria))
                    {}   
                    else
                    {
                        opcion = new Option(categoria,categoria);
                        agregadosC.push(categoria);
                        categorias.add(opcion,undefined);
                    }                           
                }
                if(grupo=="")
                {
                    categorias.innerHTML="";
                    opcion = new Option("Elegir una categoria","");
                    opcion.defaultSelected= true;
                    categorias.add(opcion,undefined);
                    categorias.disabled=false;
                    agregadosC =[]; 
                }
            }
            if(partes.length==2)
            {
                agregadosC =[];

                if(grupoT==grupo)
                { 
                    categorias.innerHTML="";
                    opcion = new Option("N/A","SIN");
                    categorias.add(opcion,undefined);
                    categorias.disabled = true;
                    if(cargado)
                    {}
                    else
                    {
                        listarNombres();
                        cargado=true;
                    }
                }
            }        
        }
}

function listarNombres(){
    nombres = document.getElementById("aName");
    categoria = document.getElementById("aCat").value;
    grupo = document.getElementById("group").value;
    nombres.innerHTML="";
    opcion = new Option("Elegir un nombre","");
    nombres.add(opcion,undefined);
    lista = []
    for(var num in todo)
        {
            partes=todo[num].split("/");
            grupoT = partes[0];
            if(partes.length==3)
            {
                categoriaT = partes[1];
                if(categoriaT==categoria)
                {
                    nombre = partes[2];
                    lista.push(nombre);
                }
                if(categoria=="")
                {
                    nombres.innerHTML="";
                    opcion = new Option("Elegir un nombre","");
                    nombres.add(opcion,undefined);
                }   
            }  
            if(partes.length==2)
            {
                if(grupo==grupoT)
                {
                    nombre = partes[1];
                    lista.push(nombre);               
                }   
            } 
        }
    lista.sort();
    for(var el in lista)
    {
        opcion = new Option(lista[el],lista[el]);
        nombres.add(opcion,undefined);
    }
    lista = []
}

function sortSelect(selElem){
    var tmpArray = new Array();
    for (var i=0;i<SelElem.options.length;i++)
    {
        tmpArray[i] = new Array();
        tmpArray[i][0] = selElem.options[i].text;
        tmpArray[i][0]
    }
}

function animation(){
    grupoA = document.getElementById("group").value;
    categoriaA = "/"+document.getElementById("aCat").value;
    nombreA = document.getElementById("aName").value;
    peticion = new XMLHttpRequest();
    if(categoriaA=="/SIN"){categoriaA="";}
    if(nombreA=="" || grupoA==""){}
    else
    {
        peticion.open("GET","animate/?animation="+grupoA+categoriaA+"/"+nombreA);
        peticion.send();
    }
}

function standard(){
    peticion = new XMLHttpRequest();
    peticion.open("GET","animate/?animation="+"Gestures"+"/"+"Maybe_1");
    peticion.send();
}