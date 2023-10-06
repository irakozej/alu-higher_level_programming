#!/usr/bin/node
// this function returns the inverse of a list

exports.esrever = function (list) {
  const rlist = [];
  while (list.length > 0) {
    rlist.push(list.pop());
  }
  return rlist;
};
