#!/usr/bin/node

exports.addMeMaybe = (x, func) => {
  x++;
  func(x);
};
