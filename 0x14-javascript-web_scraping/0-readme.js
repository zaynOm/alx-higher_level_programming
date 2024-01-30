#!/usr/bin/node
import { argv } from 'process';
import { readFile } from 'fs';

readFile(argv[2], 'utf-8', (err, data) => {
  if (err) throw err;
  console.log(data + '\n');
});
