

let name= String(prompt("name"))

let age= Number(prompt("age"))



if(age >= 18){
    console.log("your name is ", name,"and you are ", String(age),"yr");
}else if (age<18 && age>=11){
    console.log("your name is ", name,"and you are ", String(age),"yr");

}else{
    console.log("you are too young")
}