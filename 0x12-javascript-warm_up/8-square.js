#!/usr/bin/node
const argv = process.argv;
const integer = parseInt(argv[2]);

if (isNaN(integer) || integer === undefined) {
  console.log('Missing size');
} else {
  for (let index = 0; index < integer; index++) {
    let manyX = '';
    for (let index2 = 0; index2 < integer; index2++) {
      manyX += 'X';
    }
    console.log(manyX);
  }
}
