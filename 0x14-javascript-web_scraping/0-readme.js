#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');
const file = argv[2];

fs.readFile(file, 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});