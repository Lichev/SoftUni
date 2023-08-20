function solve(arr) {
  let obj = {};
  let control = {
    IN: (car) => (obj[car] = 0),
    OUT: (car) => delete obj[car],
  };
  for (let track of arr) {
    let [command, car] = track.split(", ");
    control[command](car);
  }

  Object.keys(obj).length === 0
    ? console.log(`Parking Lot is Empty`)
    : Object.entries(obj)
        .sort((a, b) => Number(a[0].slice(2, 6)) - Number(b[0].slice(2, 6)))
        .forEach(([key, value]) => console.log(`${key}`));
}

solve([
  "IN, CA2844AA",
  "IN, CA1234TA",
  "OUT, CA2844AA",
  "IN, CA9999TT",
  "IN, CA2866HI",
  "OUT, CA1234TA",
  "IN, CA2844AA",
  "OUT, CA2866HI",
  "IN, CA9876HH",
  "IN, CA2822UU",
    "OUT, CA2866HI",
    "IN, CA9876HH",
    "IN, CA2822UU",
    "OUT, CA2866HI",
    "IN, CA9876HH",
    "IN, CA2822UU",
    "OUT, CA2844AA",
    "OUT, CA2844AA",
    "OUT, CA2844AA",
]);

solve(["IN, CA2844AA", "IN, CA1234TA", "OUT, CA2844AA", "OUT, CA1234TA"]);
