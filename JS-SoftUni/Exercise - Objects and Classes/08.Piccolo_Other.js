function solve(input) {
  let lst = [];

  let action = {
    IN: (plate) => !lst.includes(plate) && lst.push(plate),
    OUT: (plate) => (lst = lst.filter((item) => item !== plate)),
  };

  for (let line of input) {
    let [command, plate] = line.split(" , ");
    action[command](plate);
  }

  lst.length === 0
    ? console.log(`Parking Lot is Empty`)
    : console.log(lst.sort().join("\n"));
}

solve([
  "IN, CA2844AA",
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
]);

solve(["IN, CA2844AA", "IN, CA1234TA", "OUT, CA2844AA", "OUT, CA1234TA"]);
