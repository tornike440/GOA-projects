let sum = 0;

for (let i = 1; i <= 60; i++) {
  if (i % 3 === 0 && i % 5 === 0) {
    sum += i;
  }
}
console.log("Sum:", sum); // გამოიტანს 15 + 30 + 45 + 60 = 150
