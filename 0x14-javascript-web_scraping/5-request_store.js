#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filepath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error, response.statusCode);
  } else {
    fs.writeFile(filepath, body, 'utf-8', error => {
      console.log(error);
    });
  }
});
