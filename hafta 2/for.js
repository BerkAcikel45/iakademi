
function clear(){
    document.getElementById("result").innerHTML = " ";
}


function loop1(){
    clear();
    for(var i = 0; i <= 10; i++)
    {
        document.getElementById("result").innerHTML += i + "<br>";
    }
}


function loop2(){
    clear();
    for(var i = 10; i > 0; i--)
    {
        document.getElementById("result").innerHTML += i + "<br>";
    }
}

function loop3(){
    clear();
    for(var i = 0; i <= 10; i++){
        document.getElementById("result").innerHTML += "Hello World" + "<br>";
    }
}

function loop4(){
    clear()
    for(var i = 1; i <= 10; i++){
        if(i % 2 === 0 ){
            document.getElementById('result').innerHTML += i + "<br>";
        }
    }
}

function loop5(){
    clear();
    for(var i = 1; i <= 100; i++){
        if(i % 3 === 0 && i % 5 === 0){
            document.getElementById('result').innerHTML += i + "<br>";
        }
    }
}

function loop6(){
    clear();
    var text = window.prompt("Enter text");
    var counter = window.prompt("Enter Quantity");
    for(var i = 1; i <= counter; i++){
        document.getElementById('result').innerHTML += text + "<br>";
    }
}

function loop7(){
    clear();
    var counter = parseInt(window.prompt("Enter Counter"));
    var a = 1;
    for(var i = 0; i < counter; i++){
        var number = parseInt(window.prompt( i + 1 + ". enter number" ));
        a *= number;
    }
    document.getElementById("result").innerHTML = a;
}

function loop8(){
    clear();
    var factorial = 1;
    var counter = parseInt(window.prompt("Enter Number"));
    for(var i = counter; i  >  0; i--)
    {
        factorial = factorial * i;
    
    }

    document.getElementById("result").innerHTML = factorial;

}

function whileloop (){
    var i = 0;
/*
    for(var i = 0; i <= 10; i+=2){

    }
    */

    while (i <= 10) {
        
        document.getElementById("result").innerHTML += i + "<br>"
        i += 2;
    }
}


function whileloop2(){
    let number = 0;
    let sum = 0;
    let avg = 0;
    let counter = 0;
    
    while (number != -1) {
        var name = window.prompt("Enter name");
        var last = window.prompt("Enter lastname");
        var age = window.prompt("Enter Age");
        alert("For exit enter -1");
        number = parseInt(window.prompt("Enter Number")); //5

    }

    document.getElementById('result').innerHTML = name + " " + last + " " + age; 
    
}