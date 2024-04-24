#!/usr/bin/node
const PSquare = require('./5-square');

class Square extends PSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let seq = '';
      for (let j = 0; j < this.width; j++) {
        seq += c;
      }
      console.log(seq);
    }
  }
}
module.exports = Square;
