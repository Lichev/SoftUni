function solve(arr) {
  const initialNumber = Number(arr[0]) + 1;
  const elements = arr.slice(1, initialNumber);
  const rest = arr.slice(initialNumber);

  let lstObj = [];

  elements.forEach((data) => {
    const [piece, composer, key] = data.split("|");

    lstObj.push(createObject(piece, composer, key));
  });

  for (const command of rest) {
    let [action, piece, composer, key] = command.split("|");

    if (action === "Add") {
      addHandler(piece, composer, key);
    } else if (action === "Remove") {
      removeHandler(piece);
    } else if (action === "ChangeKey") {
      changeHandler(piece, composer);
    } else if (action === "Stop") {
      lstObj.forEach((obj) =>
        console.log(
          `${obj.piece} -> Composer: ${obj.composer}, Key: ${obj.key}`
        )
      );
    }
  }

  function addHandler(piece, composer, key) {
    const musicObject = createObject(piece, composer, key);
    let valid = true;

    for (const song of lstObj) {
      if (song.piece === piece) {
        console.log(`${piece} is already in the collection!`);
        valid = false;
      }
    }

    if (valid) {
      console.log(`${piece} by ${composer} in ${key} added to the collection!`);
      lstObj.push(musicObject);
    }
  }

  function removeHandler(piece) {
    const isPresent = lstObj.some((obj) => obj.piece === piece);

    if (isPresent) {
      lstObj = lstObj.filter((obj) => obj.piece !== piece);
      console.log(`Successfully removed ${piece}!`);
    } else {
      console.log(
        `Invalid operation! ${piece} does not exist in the collection.`
      );
    }
  }

  function changeHandler(piece, newKey) {
    const isPresent = lstObj.some((obj) => obj.piece === piece);

    if (isPresent) {
      for (const obj of lstObj) {
        if (obj.piece === piece) {
          obj.key = newKey;
          console.log(`Changed the key of ${piece} to ${newKey}!`);
        }
      }
    } else {
      console.log(
        `Invalid operation! ${piece} does not exist in the collection.`
      );
    }
  }

  function createObject(piece, composer, key) {
    const musicObject = {
      piece,
      composer,
      key,
    };

    return musicObject;
  }
}
//
// solve([
//   "3",
//   "Fur Elise|Beethoven|A Minor",
//   "Moonlight Sonata|Beethoven|C# Minor",
//   "Clair de Lune|Debussy|C# Minor",
//   "Add|Sonata No.2|Chopin|B Minor",
//   "Add|Hungarian Rhapsody No.2|Liszt|C# Minor",
//   "Add|Fur Elise|Beethoven|C# Minor",
//   "Remove|Clair de Lune",
//   "ChangeKey|Moonlight Sonata|C# Major",
//   "Stop",
// ]);

solve([
  '4',
  'Eine kleine Nachtmusik|Mozart|G Major',
  'La Campanella|Liszt|G# Minor',
  'The Marriage of Figaro|Mozart|G Major',
  'Hungarian Dance No.5|Brahms|G Minor',
  'Add|Spring|Vivaldi|E Major',
  'Remove|The Marriage of Figaro',
  'Remove|Turkish March',
  'ChangeKey|Spring|C Major',
  'Add|Nocturne|Chopin|C# Minor',
  'Stop'
])
