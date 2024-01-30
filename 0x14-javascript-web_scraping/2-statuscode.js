#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');

request(argv[2], (_, res) => {
  console.log(`code: ${res.statusCode}`);
});
