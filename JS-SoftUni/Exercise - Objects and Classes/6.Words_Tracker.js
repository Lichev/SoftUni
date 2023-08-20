function solve(arr) {
  let words = arr[0].split(" ");
  let obj = {};

  for (let word of words) {
    obj[word] = 0;
  }

  for (let arrElement of arr.slice(1)) {
    if (arrElement in obj) {
      obj[arrElement] += 1;
    }
  }

  let sortable = []
  for (let line in obj){
    sortable.push([line, obj[line]])
  }

  sortable = sortable.sort( )


  for (let x of sortable) {
    console.log(`${x[0]} - ${x[1]}`)
  }
}



solve([
  'is the',
  'first', 'sentence', 'Here', 'is',
  'another', 'the', 'And', 'finally', 'the',
  'the', 'sentence'])