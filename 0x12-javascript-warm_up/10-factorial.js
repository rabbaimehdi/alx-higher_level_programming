#!/usr/bin/node
const argv = process.argv;
const a = parseInt(argv[2]);

function factorial(a) {
  if (a <= 1 || isNaN(a)) {
    return 1;
  }
  else {
    return a * factorial(a-1);
  }
}
console.log(factorial(a));
