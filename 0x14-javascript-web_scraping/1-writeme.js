#!/usr/bin/node
const { argv } = require('process');
const { writeFile } = require('fs');

writeFile(argv[2], argv[3], 'utf-8', (err) => {
  if (err) throw err;
});
