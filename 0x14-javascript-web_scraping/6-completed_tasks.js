#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

request(argv[2], (err, res, body) => {
  if (err) return console.log(err);
  const data = JSON.parse(body);
  const tt = data.map(todo =>{
    if (todo.completed)
      return todo
  });
});
