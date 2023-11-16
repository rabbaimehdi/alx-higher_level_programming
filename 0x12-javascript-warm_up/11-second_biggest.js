#!/usr/bin/node
const argv = process.argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  const list = argv.slice(2);
  list.sort();
  console.log(list[1]);
}
