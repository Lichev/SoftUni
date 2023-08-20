function solve(input) {
  let addressBook = {};

  for (const line of input) {
    let [name, number] = line.split(":");
    addressBook[name] = number;
  }

  let sortedEntries = Object.entries(addressBook).sort(
    ([keyA, valueA], [keyB, valueB]) => keyA.localeCompare(keyB)
  );

  for (let [key, value] of sortedEntries) {
    console.log(`${key} -> ${value}`);
  }



}

solve([
  "Tim:Doe Crossing",
  "Bill:Nelson Place",
  "Peter:Carlyle Ave",
  "Bill:Ornery Rd",
]);
