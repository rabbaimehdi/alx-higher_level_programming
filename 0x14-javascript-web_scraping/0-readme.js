#!/usr/bin/node
const fs = require('fs');
const process = require('process');

const readAndPrintFile = (filePath) => {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.log(`${err}`);
    } else {
      console.log(data);
    }
  });
};

const filePath = process.argv[2];
readAndPrintFile(filePath);
