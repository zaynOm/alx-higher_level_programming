#!/usr/bin/node

const { argv } = require('node:process');

const s = argv.length > 3 ? 's' : '';
if (argv.length > 2) console.log(`Argument${s} found`);
else console.log('No argument');
