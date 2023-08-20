function solve(txt) {
  let words = txt.split(" ").map((x) => x.toLowerCase());
  let obj = {};
  words.forEach((x) => (obj[x] = 0));
  words.forEach((word) => obj[word] !== undefined && obj[word]++);
  let lst = [];
  for (let key in obj) {
    let value = obj[key];
    if (value % 2 !== 0) {
      lst.push(key);
    }
  }

  console.log(lst.join(" "));
}

solve("Cake IS SWEET is Soft CAKE sweet Food");
