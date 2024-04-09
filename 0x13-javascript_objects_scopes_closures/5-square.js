#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size);
    this.size = size;
  }

  print () {
    super.print();
    let i = 0;
    while (i < this.size) {
      console.log('X'.repeat(this.size));
      i += 1;
    }
  }

  double () {
    super.double();
    this.size *= 2;
  }
}
module.exports = Square;
