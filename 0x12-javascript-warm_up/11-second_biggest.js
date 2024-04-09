#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let i = 2;
  const arr = [];
  while (i < process.argv.length) {
    arr.push(parseInt(process.argv[i]));
    i += 1;
  }
  arr.sort();
  console.log(arr[arr.length - 1]);
}
