#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3] + '\n', function (err) {
  if (err) {
    console.error(err);
  }
});
