#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');

url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`

request(url, (_, res) => {
  console.log(res.body.title);
});
