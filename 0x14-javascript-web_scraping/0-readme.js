#!/usr/bin/node
const { argv } = require('node:process');
const { readFile } = require('node:fs');

readFile(argv[2], 'utf-8', (err, data) => {
    if (err) {
        return console.log(err);
    }
    console.log("Body: ", data);
})
