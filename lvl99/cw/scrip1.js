for (let i = 0; i <= 100; i++) {
  if (i % 2 === 0) {
    console.log(String(i) + " - ლუწი");
  }
}

for (let i = 1; i <= 100; i++) {
    if (i % 2 !== 0) {
        console.log(String(i) + " - კენტი");
    }
}

for (let i = 0; i <= 100; i++) {
    if (i % 2 === 0) {
        console.log(String(i) + " - ლუწი");
    } else {
        console.log(String(i) + " - კენტი");
    }
  
}


let a=0
for (let i = 1; i <= 30; i++) {
    if (i % 2 === 0) {
        a = a + i

    }

}

console.log(a)




let c = Number(prompt("შეიყვანეთ რიცხვი"))

let b= Number(prompt("შეიყვანეთ რიცხვი"))

if (b > c) {
    for (let i = c; i <= b; i++) {
    console.log(i)
    }
}elif (c > b) {
    for (let i = b; i <= c; i++) {
    console.log(i)
    }
}
