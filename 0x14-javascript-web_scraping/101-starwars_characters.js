#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request(url, (err, _, body) => {
  if (err) throw err;
  const characters = JSON.parse(body).characters;
  for (const charUrl of characters) {
    request(charUrl, async (err, _, body) => {
      if (err) throw err;
      const person = await JSON.parse(body);
      console.log(await person.name);
    });
  }
});
