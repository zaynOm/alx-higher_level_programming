#!/usr/bin/node
const { argv } = require("process");
const request = require("request");

request(argv[2], (err, res, body) => {
  if (err) return console.log(err);
  const data = JSON.parse(body).results;
  let count = 0;
  for (const film of data) {
    for (const character of film.characters) {
      if (/.*\/18\//g.test(character)) count++;
    }
  }
  console.log(count);
});
