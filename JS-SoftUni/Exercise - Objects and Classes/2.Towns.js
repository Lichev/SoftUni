function solve(arr) {
  for (let arrElement of arr) {
    let arrSplit = arrElement.split(" | ");
    let town = arrSplit[0]
    let latitude = Number(arrSplit[1])
    let longitude = Number(arrSplit[2])
    let obj = {
      town,
      latitude: latitude.toFixed(2),
      longitude: longitude.toFixed(2),
    };

    console.log(obj)
  }
}

solve(["Sofia | 42.696552 | 23.32601", "Beijing | 39.913818 | 116.363625"]);
