#!/usr/bin/node

const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c = 'X') {
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
