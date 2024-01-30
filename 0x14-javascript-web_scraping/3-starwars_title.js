#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request(url, (err, _, body) => {
  if (err) console.log(err);
  console.log(JSON.parse(body).title);
});