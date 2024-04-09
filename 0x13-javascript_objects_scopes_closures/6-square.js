#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i = 0;
    while (i < this.height) {
      console.log(c.repeat(this.width));
      i += 1;
    }
  }
}
module.exports = Square;
