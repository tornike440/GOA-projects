let start = Number(prompt("Enter start number"));
let end = Number(prompt("Enter end number"));

let sum = 0;

for (let i = start; i <= end; i++) {
  if (i % 2 === 0) {
    sumEven += i;
  }
}

console.log("ლუწი რიცხვების ჯამი:", sumEven);
