function solve(arr) {
  let employees = {};

  for (let employee of arr) {
    employees[employee] = employee.length;
  }

  Object.keys(employees).forEach((key) =>
    console.log(`Name: ${key} -- Personal Number: ${employees[key]}`)
  );
}

solve([
  "Silas Butler",
  "Adnaan Buckley",
  "Juan Peterson",
  "Brendan Villarreal",
]);
