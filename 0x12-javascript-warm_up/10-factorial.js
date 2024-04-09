#!/usr/bin/node
function fact (a) {
  if (a === 0) {
    return 1;
  }
  return a * fact(a - 1);
}
if (parseInt(process.argv[2])) {
  const a = parseInt(process.argv[2]);
  console.log(fact(a));
} else {
  console.log(1);
}
