#!/usr/bin/node
const fs = require('fs');
const process = require('process');

const writefile = (filepath, data) => {
  fs.writeFile(filepath, data, 'utf-8', err => {
    if (err) {
      console.log(err);
    }
  }
  );
};

const filepath = process.argv[2];
const data = process.argv[3];
writefile(filepath, data);
