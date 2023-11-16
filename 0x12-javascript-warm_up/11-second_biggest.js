#!/usr/bin/node
const argv = process.argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  const list = argv.slice(2).map(Number);
  list.sort((a, b) => (a - b));
  console.log(list[list.length - 2]);
}
