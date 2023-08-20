function solve(arr) {
  let lstObj = [];

  for (let arrElement of arr) {
    let [Hero, level, Items] = arrElement.split(" / ");

    let obj = {
      Hero,
      level: Number(level),
      Items,
    };
    lstObj.push(obj);
  }

  let filtered = lstObj.sort((a, b) => a.level - b.level);

  for (let i = 0; i < lstObj.length; i++) {
    console.log(`Hero: ${lstObj[i].Hero}`);
    console.log(`level => ${lstObj[i].level}`);
    console.log(`items => ${lstObj[i].Items}`);
  }
}

solve([
  "Isacc / 25 / Apple, GravityGun",
  "Derek / 12 / BarrelVest, DestructionSword",
  "Hes / 1 / Desolator, Sentinel, Antara",
]);
