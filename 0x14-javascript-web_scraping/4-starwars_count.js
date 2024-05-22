#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) console.log(error);
  const re = JSON.parse(body);
  let ch = 0;
  for (let i = 0; i < re.results.length; i++) {
    for (let j = 0; j < re.results[i].characters.length; j++) {
      if (re.results[i].characters[j].includes('18')) {
        ch++;
      }
    }
  }
  console.log(ch);
});
