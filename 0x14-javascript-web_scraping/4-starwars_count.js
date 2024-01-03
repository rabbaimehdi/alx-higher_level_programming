#!/usr/bin/node
const request = require('request');
const process = require('process');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error, response.statusCode);
  } else {
    body = JSON.parse(body);
    let counter = 0;
    body.results.forEach(element => {
      if (element.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        counter += 1;
      }
    }
    );
    console.log(counter);
  }
});
