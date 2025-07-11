#!/usr/bin/node

const { argv } = require('node:process');
const converted = parseInt(argv[2]);

if (isNaN(converted)) {
  console.log('Not a number');
} else console.log('My number:', argv[2]);
