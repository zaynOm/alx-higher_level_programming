#!/usr/bin/node

const { argv } = require('process');

if (argv.length > 3) console.log(argv.slice(2).sort((a, b) => b - a)[1]);
else console.log(0);
