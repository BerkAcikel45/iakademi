
var array = [];
var arr = new Array();

function concat(){
    let names = new Array();
    names.push("Berk");
    names.push("Acık");

    let names2 = new Array();
    names2.push("Ali");
    names2.push("Veli");

    let names3 = names.concat(names2);

    /*
    for(var i = 0; i > names.length;i++){
        names3 = names.push(names2[i]);
    }
    */

    alert(names3);
}


function every(){
    function isBigger(age, index, array){
        console.log(index);
        console.log(array)
        return age >= 20;
    }

    let ages = [20, 3, 40, 60].every(isBigger);
    let ages2 = [20, 45, 55, 35].every(isBigger);
    
    alert(ages);
    alert(ages2);

}

function filter(){
    function bigNumber(number){
        return number >= 25;
    }

    let bigNumberList = [12,20,56,77,45,5].filter(bigNumber);
    alert(bigNumberList);

}

function foreach(){
    let fruits = ["apple", "orange", "cherry"];
    let result = "";
    fruits.forEach(eachValue);


    function eachValue(item, index){
        result += index + " : " + item + "     ";
    }

    alert(result);
}