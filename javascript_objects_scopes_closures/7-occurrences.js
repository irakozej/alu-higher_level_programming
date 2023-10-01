#!/usr/bin/node
// this function returns number of occurrences in one list

exports.nbOccurences = function (list, searchElement) {
  return list.filter((value) => (value === searchElement)).length;
};
