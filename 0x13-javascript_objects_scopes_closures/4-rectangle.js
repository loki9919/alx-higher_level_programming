#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rec = '';
      for (let j = 0; j < this.width; j++) {
        rec += 'X';
      }
      console.log(rec);
    }
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    const rot = this.width;
    this.width = this.height;
    this.height = rot;
  }
}
module.exports = Rectangle;
