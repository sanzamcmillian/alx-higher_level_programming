#!/usr/bin/node
const [,, arg] = process.argv;
if (!arg && arg !== '') {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
