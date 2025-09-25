let start = Number(prompt("Enter start number"));
let end = Number(prompt("Enter end number"));

let evenCount = 0;
let oddCount = 0;

for (let i = start; i <= end; i++) {
  if (i % 2 === 0) {
    evenCount++;
  } else {
    oddCount++;
  }
}

console.log("ლუწების რაოდენობა: " + evenCount + ", კენტების რაოდენობა: " + oddCount);
