#!/usr/bin/node
const Square_ = require('./5-square.js');

class Square extends Square_ {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        let printChar = '';
        for (let j = 0; j < this.height; j++) {
          printChar += c;
        }
        console.log(printChar);
      }
    }
  }
}
module.exports = Square;
