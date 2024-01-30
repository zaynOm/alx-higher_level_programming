#!/usr/bin/node
const { argv } = require('process')
const request = require('request')

request(argv[2], (err, res, body) => {
  // TODO: fix this to quit after loging the error
  if (err) console.log(err);
  data = JSON.parse(body).results;
  console.log(data);
});
