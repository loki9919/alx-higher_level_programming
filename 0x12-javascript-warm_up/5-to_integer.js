#!/usr/bin/node
// print the first argument can be converted to an integer
if (!isNaN(parseInt(process.argv[2]))) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
