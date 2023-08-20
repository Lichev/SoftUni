function solve(arr) {
  let horses = Array.from(arr[0].split("|"));
  let rest = Array.from(arr.slice(1));
  // console.log(horses)

  for (const element of rest) {
    let data = Array.from(element.split(" "));
    let action = data[0];

    if (action === "Retake") {
      let overtakingHorse = data[1];
      let overtakenHorse = data[2];

      let indexTaking = horses.indexOf(overtakingHorse);
      let indexTaken = horses.indexOf(overtakenHorse);

      if (indexTaking < indexTaken) {
        [horses[indexTaking], horses[indexTaken]] = [
          horses[indexTaken],
          horses[indexTaking],
        ];
        console.log(`${overtakingHorse} retakes ${overtakenHorse}.`);
        // console.log(horses)
      }
    } else if (action === "Trouble") {
      let horse = data[1];
      let index = horses.indexOf(horse);

      if (index > 0) {
        [horses[index], horses[index - 1]] = [horses[index - 1], horses[index]];
        console.log(`Trouble for ${horse} - drops one position.`);
        // console.log(horses);
      }
    } else if (action === "Rage") {
      const horse = data[1]
      const idx = horses.indexOf(horse)
      horses.splice(idx, 1)
      horses.splice(idx + 2, 0, horse)
      console.log(`${horse} rages 2 positions ahead.`)

      // console.log(horses)
    } else if (action === "Miracle") {
      let firstHorse = horses.shift();
      horses.push(firstHorse);
      console.log(`What a miracle - ${firstHorse} becomes first.`);
      // console.log(horses)
    } else if (action === "Finish") {
      break;
    }
  }

  console.log(horses.join("->"));
  console.log(`The winner is: ${horses[horses.length - 1]}`);
}

solve([
  "Onyx|Domino|Sugar|Fiona",

  "Trouble Onyx",

  "Retake Onyx Sugar",

  "Rage Domino",

  "Miracle",

  "Finish",
]);
