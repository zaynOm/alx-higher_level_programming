#!/usr/bin/node

const { argv } = require('process');

let nums = argv.slice(2);
nums.sort().reverse();
if (nums.length < 2) nums = [0, 0];
console.log(nums[1]);
