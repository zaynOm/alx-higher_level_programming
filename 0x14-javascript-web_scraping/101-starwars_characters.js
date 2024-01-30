#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request(url, async (err, _, body) => {
  if (err) throw err;

  const characters = JSON.parse(body).characters;
  for (const charUrl of characters) {
    const { name } = await new Promise((resolve, reject) => {
        request(charUrl, (err, _, body) => {
          if (err) reject(err);
          resolve(JSON.parse(body));
        });
    });
    console.log(name);
  }
});
