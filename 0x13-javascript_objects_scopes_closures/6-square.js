#!/usr/bin/node
const Square1 = require('./5-square');
class Square extends Square1 {
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
