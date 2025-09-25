let input = prompt("Enter something");

// prompt ყოველთვის აბრუნებს string-ს.
// ვცადოთ გადავაქციოთ რიცხვად:
let num = Number(input);

if (isNaN(num)) {
  // თუ NaN გამოვიდა, ესეიგი ტექსტია
  console.log("you entered string number, so you are wrong");
} else {
  // თუ რიცხვია
  for (let i = 1; i <= num; i++) {
    if (i % 2 !== 0) {
      console.log(i);
    }
  }
}

