#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((l) => {
    if (l === searchElement) count++;
  });
  return count;
};
