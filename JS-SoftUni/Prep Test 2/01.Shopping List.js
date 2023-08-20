function solve(arr) {
  let productList = Array.from(arr[0].split("!"));
  let actions = arr.slice(1)


  for (const action of actions) {
    let data = action.split(" ");
    let command = data[0]

    if (command === 'Urgent'){
      urgent(data[1])
    } else if (command === 'Unnecessary') {
      unnecessary(data[1])
    } else if (command === 'Correct') {
      correct(data[1], data[2])
    } else if (command === 'Rearrange') {
      rearrange(data[1])
    }
  }

  console.log(productList.join(', '))

  function rearrange(item){
    if (productList.includes(item)){
      let index = productList.indexOf(item);
      productList.splice(index, 1);
      productList.push(item)
    }
  }

  function correct(oldItem, newItem){
    if (productList.includes(oldItem)){
      let index = productList.indexOf(oldItem)
      productList[index] = newItem
    }
  }

  function urgent(item){
    if (!productList.includes(item)){
      productList.unshift(item)
    }
  }

  function unnecessary(item){
    if (productList.includes(item)){
      const index = productList.indexOf(item)
      productList.splice(index,1)
    }
  }

}

dict = {
  key: value,
  dannisdas: [Rado, Joro]
}

print(dict['danni'])


solve([
  "Milk!Pepper!Salt!Water!Banana",
  "Urgent Bob",
  "Unnecessary Bob",
  "Correct Pepper Onion",
  "Rearrange Grapes",
  "Correct Tomatoes Potatoes",
  "Go Shopping!",
]);

solve()
