#!/usr/bin/node
const { readFile } = require('fs');
const { argv } = require('process');

readFile(argv[2], 'utf-8', (err, data) => {
  if (err) throw err;
  console.log(data + '\n');
});
