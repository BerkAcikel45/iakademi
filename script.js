alert("Hello World");

var a;
var b;

a = 10;
b = 5;

var sum;

sum = a + b;



alert(sum);

var names = ['John', 'Smith', 'Ali'];
var years = new Array(1990, 1995, 2000);


var student = {
    id:1,
    name: "Berk",
    surname: "Açıkel",
    age:15,
}

alert("Student : { id: " + student.id + " name: " +
        student.name + "surname: " + student.surname + " age:" + student.age + "}");


/* 
while (true) {
    var name = prompt("What is the name ");
    if(name == "Berk")
    {
        var lastName = prompt("What is Last Name");
        if (lastName == "Açıkel"){
            alert("Student : { id: " + student.id + " name: " +
            student.name + "surname: " + student.surname + " age:" + student.age + "}");
            break;
        }
    }
}

*/


while (true) {
    var name = prompt("What is the name ");
    var lastName = prompt("What is lastName ");
    if(name == "Berk" && lastName == 'Açıkel'){
        alert("Student : { id: " + student.id + " name: " +
        student.name + "surname: " + student.surname + " age:" + student.age + "}");
        break;
    }

}