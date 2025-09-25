let start = Number(prompt("Enter start number"));
let end = Number(prompt("Enter end number"));

let sum = 0;
let count = 0;

for (let i = start; i <= end; i++) {
  sum += i;
  count++;
}

let avg = sum / count;

console.log("ჯამი: " + sum);
console.log("საშუალო: " + avg);
