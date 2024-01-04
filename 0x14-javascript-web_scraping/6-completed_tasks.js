#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const dict = {
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0,
  7: 0,
  8: 0,
  9: 0,
  10: 0
};
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(body);
    body.forEach(todo => {
      if (todo.completed) {
        dict[todo.userId] += 1;
      }
    });
    console.log(dict);
  }
});
