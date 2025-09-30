let score = Number(prompt("Enter your score (0-100)"));

if (score < 0 || score > 100) {
  console.log("არასწორი მონაცემი");
} else if (score < 50) {
  console.log("ჩაიჭერი");
} else if (score <= 69) {
  console.log("საშუალო");
} else if (score <= 89) {
  console.log("კარგი");
} else {
  console.log("ძალიან კარგი");
}










let a = Number(prompt("Enter first number"));
let b = Number(prompt("Enter second number"));
let c = Number(prompt("Enter third number"));

// ყველაზე დიდი და პატარა
let max = Math.max(a, b, c);
let min = Math.min(a, b, c);

console.log("ყველაზე დიდი რიცხვი:", max);
console.log("ყველაზე პატარა რიცხვი:", min);

// ლუწობა/კენტობა
if (max % 2 === 0) {
  console.log("ყველაზე დიდი რიცხვი ლუწია");
} else {
  console.log("ყველაზე დიდი რიცხვი კენტია");
}
