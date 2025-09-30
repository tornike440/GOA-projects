let num = Number(prompt("Enter a number"));
let luwi = 0;
let kenti = 0;

for (let i = 1; i <= num; i++) {
  if (i % 2 === 0) {
    luwi++;
  } else {
    kenti++;
  }
}

console.log("ლუწების რაოდენობა:", luwi, "კენტების რაოდენობა:", kenti);
