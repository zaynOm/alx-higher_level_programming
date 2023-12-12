#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  list.forEach((l) => rev.unshift(l));
  return rev;
};
