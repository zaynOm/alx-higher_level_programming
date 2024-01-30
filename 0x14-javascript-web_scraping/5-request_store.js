#!/usr/bin/node
const { argv } = require('process');
const request = require('request');
const { writeFile } = require('fs');

request(argv[2], (err, _, body) => {
  if (err) return console.log(err);
  writeFile(argv[3], body, 'utf-8', (err) => {
    if (err) return console.log(err);
  });
});
