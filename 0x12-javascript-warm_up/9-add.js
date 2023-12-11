#!/usr/bin/node

const { argv } = require('process');

function add (a, b) { console.log(parseInt(a) + parseInt(b)); }
add(argv[2], argv[3]);
