#!/usr/bin/node
const argv = process.argv;
const integer = parseInt(argv[2]);

if (isNaN(integer) || integer === undefined) {
	  console.log('Missing number of occurrences');
} else {
	for (let index = 0; index < integer; index++) {
		    console.log('C is fun');
	}
}
