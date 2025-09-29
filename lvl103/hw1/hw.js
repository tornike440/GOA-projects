
function sumArray(arr) {
  let sum = 0;
  for (let num of arr) {
    sum += num;
  }
  return sum;
}

function countEvenOdd(arr) {
  let even = 0, odd = 0;
  for (let num of arr) {
    if (num % 2 === 0) {
      even++;
    } else {
      odd++;
    }
  }
  return ("ლუწი:", even, "კენტი:", odd);
}

function findMax(arr) {
  let max = arr[0];
  for (let num of arr) {
    if (num > max) {
      max = num;
    }
  }
  return max;
}


function findMin(arr) {
  let min = arr[0];
  for (let num of arr) {
    if (num < min) {
      min = num;
    }
  }
  return min;
}

function average(arr) {
  return sumArray(arr) / arr.length;
}

function modifyArray() {
  let arr = ["გიორგი", 14, "საბა", 90.5, "ირაკლი", true];
  arr[3] = 10.89;
  arr[5] = false;
  arr[1] = "ირაკლი";
  return(arr);
}

function printElements(arr) {
  for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
  }
}


function countStringsAndSumIntegers(arr) {
  let stringCount = 0;
  let intSum = 0;
  for (let item of arr) {
    if (typeof item === "string") {
      stringCount++;
    } else if (typeof item === "number") {
      intSum += item;
    }
  }
  return("სტრინგების რაოდენობა:", stringCount, "ინტეჯერების ჯამი:", intSum);
}


function evenCountOddSum(arr) {
  let even = 0;
  let oddSum = 0;
  for (let num of arr) {
    if (num % 2 === 0) {
      even++;
    } else {
      oddSum += num;
    }
  }
  return("ლუწების რაოდენობა:", even, "კენტების ჯამი:", oddSum);
}

function replaceStringsWithTrue(arr) {
  for (let i = 0; i < arr.length; i++) {
    if (typeof arr[i] === "string") {
      arr[i] = true;
    }
  }
  return arr;
}




