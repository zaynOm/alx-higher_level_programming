#!/usr/bin/node

const { argv } = require('process');
const n = parseInt(argv[2]);
function factorial (x) {
  if (x <= 1) return 1;
  return x * factorial(--x);
}
if (n) console.log(factorial(n));
else console.log(1);
