#!/usr/bin/node
const list = require('./100-data').list;
const newlist = list.map(function (number, index) {
  return number * index;
});

console.log(list);
console.log(newlist);
