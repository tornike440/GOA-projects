//8)მომხმარებელს შემოატანინეთ თქვენი სახელი,გვარი,ასაკი,საცხოვრებელი ადგილი,დაბადების თარიღი(წლებში),სიმაღლე ,წონა და შეინახეთ ცვლადებში ,გამოიყენეთ prompt ფუნქცია,

let firstName = prompt("Enter your first name:");
let lastName = prompt("Enter your last name:");
let age = prompt("Enter your age:");
while (Number(age) <= 0 ) {
    age = prompt("Please enter a valid age:");
}
let city = prompt("Enter your city of residence:");
let birthYear = prompt("Enter your birth year:");
while (Number(birthYear) <= 1900 ) {
    birthYear = prompt("Please enter a valid birth year:");
}
let height = prompt("Enter your height in cm:");
while (Number(height) <= 140 ) {
    height = prompt("Please enter a valid height:");
}
let weight = prompt("Enter your weight in kg:");
while (Number(weight) <= 30 ) {
    weight = prompt("Please enter a valid weight:");
}

console.log("First Name:", firstName);
console.log("Last Name:", lastName);
console.log("Age:", age);
console.log("City of Residence:", city);
console.log("Birth Year:", birthYear);
console.log("Height (cm):", height);
console.log("Weight (kg):", weight);
