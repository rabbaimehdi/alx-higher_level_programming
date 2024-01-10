#!/usr/bin/node
const request = require('request');
const characterId = '18';
const url = process.argv[2];
let counter = 0;

request(url, (error, response, body) => {
  if (error) {
    console.log(error, response.statusCode);
  } else {
    body = JSON.parse(body);
    body.results.forEach(film => {
      film.characters.forEach(character => {
        if (character.includes(characterId)) {
          counter += 1;
        }
      });
    }
    );
    console.log(counter);
  }
});
