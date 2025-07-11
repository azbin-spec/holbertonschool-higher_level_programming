#!/usr/bin/node

const { argv } = require('node:process');
const size = argv.length;
let x = 0;

function toInt (item, index, arr) {
  arr[index] = parseInt(arr[index]);
}

function findSecond (arr) {
  let max = 0;
  let second = 0;
  for (let i = 2; i < arr.length; i++) {
    if (arr[i] >= max) {
      second = max;
      max = arr[i];
    } else if (arr[i] > second) {
      second = arr[i];
    }
  }
  return second;
}

if (size > 3) {
  argv.forEach(toInt);
  x = findSecond(argv);
}

console.log(x);
