#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

request(argv[2], (err, res, body) => {
  if (err) return console.log(err);
  const data = JSON.parse(body);
  const dict = {};
  for (const todo of data) {
    const id = todo.userId;
    if (todo.completed) {
      dict[id] = (dict[id] || 0) + 1;
    }
  }
  console.log(dict);
});
