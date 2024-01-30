#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

request(argv[2], (_, res) => {
  console.log(`code: ${res.statusCode}`);
});
