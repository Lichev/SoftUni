function getInfo() {
  let busID = document.getElementById("stopId").value;
  let stopName = document.getElementById("stopName");
  let busPrint = document.getElementById("buses");
  let BASE_URL = "http://localhost:3030/jsonstore/bus/businfo/";

  while (busPrint.firstChild) {
    busPrint.removeChild(busPrint.firstChild);
  }
  ``;
  fetch(`${BASE_URL}${busID}`)
    .then((res) => res.json())
    .then((busInfo) => {
      let { buses, name } = busInfo;
      stopName.textContent = name;
      for (let busesKey in buses) {
        let li = document.createElement("li");
        li.textContent = `Bus ${busesKey} arrives in ${buses[busesKey]} minutes`;
        busPrint.appendChild(li);
      }
    })
    .catch((err) => {
      stopName.textContent = "Error";
    });
}
