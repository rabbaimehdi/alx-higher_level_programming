#!/usr/bin/node
const request = require('request');
const process = require('process');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error, response.statusCode);
  } else {
    body = JSON.parse(body);
    console.log(body.title);
  }
});
