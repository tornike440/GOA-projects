let myName = "Tornike";
let guess;
let attempts = 0;

while (guess !== myName){
  guess = prompt("Enter my name:");
  attempts++;
} ;

console.log("you guessed my name and your attempts is:", attempts);
