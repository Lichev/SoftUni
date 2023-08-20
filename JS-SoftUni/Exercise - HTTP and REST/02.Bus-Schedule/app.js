function solve() {
  let arriveBtn = document.getElementById('arrive');
  let departBtn = document.getElementById('depart');
  let info = document.querySelector('.info')
  let lastStop = 'depot'
  let GET_URL = 'http://localhost:3030/jsonstore/bus/schedule/'


  let currentStation;
  let nextStation = 'depot';

  function getData(url, lastStop){
    fetch(`${GET_URL}${lastStop}`)
      .then((response) => response.json())
      .then((data) => {
        currentStation = data["name"];
        nextStation = data["next"]
        console.log(currentStation);
        console.log(nextStation)
      })
      .catch((err) => console.log(`error`));
  }
  function depart() {
    getData(GET_URL, nextStation)
    info.textContent = `Next stop ${currentStation ? `${currentStation}` : 'Depot'}`
    arriveBtn.disabled = false
    departBtn.disabled = true
  }

  async function arrive() {

    info.textContent = `Arriving at ${currentStation}`
    arriveBtn.disabled = true
    departBtn.disabled = false
    getData(GET_URL, nextStation)
  }

  return {
    depart,
    arrive,
  };
}

let result = solve();
