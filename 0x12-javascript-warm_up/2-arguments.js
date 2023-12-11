#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length > 2) console.log('Argumrnt found');
else console.log('No argument');
