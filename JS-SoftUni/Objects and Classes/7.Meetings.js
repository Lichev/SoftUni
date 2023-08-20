function solve(arr) {
  let meetings = {};
  for (let line of arr) {
    let [weekday, name] = line.split(" ");

    if (meetings.hasOwnProperty(weekday)) {
      console.log(`Conflict on ${weekday}!`);
    } else {
      meetings[weekday] = name;
      console.log(`Scheduled for ${weekday}`);
    }
  }

  for (let day in meetings) {
    console.log(`${day} -> ${meetings[day]}`);
  }
}

solve([
  "Friday Bob",
  "Saturday Ted",
  "Monday Bill",
  "Monday John",
  "Wednesday George",
]);
