#!/usr/bin/node
const { argv } = require('process');
const { readFile } = require('fs');

readFile(argv[2], 'utf-8', (err, data) => {
  if (err) throw err;
  console.log(data + '\n');
});
