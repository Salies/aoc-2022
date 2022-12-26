const fs = require('node:fs');
const readline = require('node:readline');

const rl = readline.createInterface({
  input: fs.createReadStream('inputs/day3.txt'),
  crlfDelay: Infinity,
});

rl.on('line', (line) => {
  // code
});