#!/usr/bin/node
if (!isNaN(parseInt(process.argv[2]))) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    let line = '';
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
