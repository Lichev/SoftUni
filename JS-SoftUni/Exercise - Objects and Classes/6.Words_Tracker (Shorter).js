function solve(arr) {
  let words = arr[0].split(" ");
  let obj = {};
  words.forEach((x) => (obj[x] = 0));

  arr.slice(1).forEach((word) => obj[word] !== undefined && obj[word]++);
  Object.entries(obj)
    .sort((a, b) => b[1] - a[1])
    .forEach(([sss, count]) => console.log(`${sss} - ${count}`));
}

solve([
  "is the",
  "first",
  "sentence",
  "Here",
  "is",
  "another",
  "the",
  "And",
  "finally",
  "the",
  "the",
  "sentence",
]);
