#!/usr/bin/node
const argv = process.argv;
const integer = parseInt(argv[2])

if (isNaN(integer) || integer === undefined) {
  console.log('Not a number');
} else {
  console.log(integer);
}
