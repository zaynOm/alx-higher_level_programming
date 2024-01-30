#!/usr/bin/node
const { argv } = require('node:process');
const { writeFile } = require('node:fs');

writeFile(argv[2], argv[3], 'utf-8', (err) => {
    throw err;
});
