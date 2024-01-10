#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const dict = {};
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(body);
    body.forEach(todo => {
      if (todo.completed) {
        if (!dict[todo.userId]) {
          dict[todo.userId] = 1;
        } else {
          dict[todo.userId] += 1;
        }
      }
    });
    console.log(dict);
  }
});
