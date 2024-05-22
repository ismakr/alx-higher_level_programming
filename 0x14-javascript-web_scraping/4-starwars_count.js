#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) console.log(error);
  const re = JSON.parse(body);
  const chr = 'https://swapi-api.alx-tools.com/api/people/18/';
  let j = 0;
  for (let i = 0; i < re.results.length; i++) {
    if (re.results[i].characters.includes(chr)) {
      j++;
    }
  }
  console.log(j);
});
