#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let index = 0; index < this.height; index++) {
      let X = '';
      for (let index2 = 0; index < this.width; index2++) {
        X += 'X';
      }
      console.log(X);
    }
  }
}
module.exports = Rectangle;
