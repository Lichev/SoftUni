function attachEvents() {
  let location = document.getElementById("location");
  let submit = document.getElementById("submit");
  let BASE_URL = "http://localhost:3030/jsonstore/forecaster/today/";

  let forecastContainer = document.getElementById("forecast");
  let current = document.getElementById("current");
  let upcoming = document.getElementById("upcoming");

  submit.addEventListener("click", submitHandler);

  function submitHandler() {
    let currentLocationCode;
    fetch("http://localhost:3030/jsonstore/forecaster/locations/")
      .then((response) => response.json())
      .then((data) => {
        let objLocation = {};
        objLocation = data;
        let currentLocationCode;

        for (const obj in objLocation) {
          if (objLocation[obj].name === location.value) {
            currentLocationCode = objLocation[obj].code;
          }
        }
        return fetch(
          `http://localhost:3030/jsonstore/forecaster/today/${currentLocationCode}`
        );
      })
      .then((response) => response.json())
      .then((data) => {
        const forecastCondition = data.forecast.condition;
        const forecastHigh = data.forecast.high;
        const forecastLow = data.forecast.low;
        const name = data.name;

        forecastContainer.style.display = "block";
        let forecastsClass = createElement("div", "", current, "", [
          "forecasts",
        ]);
        let weatherSym = weatherSymbol(forecastCondition);
        let conditionSymbol = createElement("span", "", forecastsClass, "", [
          "condition",
          "symbol",
        ]);
        conditionSymbol.innerHTML = weatherSym;
        let spanCondition = createElement("span", "", forecastsClass, "", [
          "condition",
        ]);
        createElement("span", name, spanCondition, "", ["forecast-data"]);
        let highLow = createElement("span", "", spanCondition, "", [
          "forecast-data",
        ]);
        highLow.innerHTML = `${forecastLow}&deg;/${forecastHigh}&deg;`;
        createElement("span", forecastCondition, spanCondition, "", [
          "forecast-data",
        ]);

        return fetch(`http://localhost:3030/jsonstore/forecaster/locations/`);
      })
      .then((response) => response.json())
      .then((data) => {
        let objLocation = {};
        objLocation = data;
        let currentLocationCode;

        for (const obj in objLocation) {
          if (objLocation[obj].name === location.value) {
            currentLocationCode = objLocation[obj].code;
          }
        }
        return fetch(
          `http://localhost:3030/jsonstore/forecaster/upcoming/${currentLocationCode}`
        );
      })
      .then((response) => response.json())
      .then((data) => {
        let forecastInfo = createElement('div', '', upcoming, '', ['forecast-info'])
        for (const forecastKey in data.forecast) {
          let cond = data.forecast[forecastKey].condition;
          let high = data.forecast[forecastKey].high;
          let low = data.forecast[forecastKey].low;

          let upcoming = createElement('span', '', forecastInfo, '', ['upcoming'])
          let weatherSum = weatherSymbol(cond)
          let symbol = createElement('span', '', upcoming, '', ['symbol'])
          symbol.innerHTML = weatherSum
          let highLow = createElement('span', '', upcoming, '', ['forecast-data'])
          highLow.innerHTML = `${low}&deg;/${high}&deg;`
          createElement('span', cond, upcoming, '', ['forecast-data'])
        }
      })
      .catch((error) => console.log("Error"));
  }

  function createElement(type, content, parentNode, id, classes, attributes) {
    const htmlElement = document.createElement(type);

    if (content && type !== "input") {
      htmlElement.textContent = content;
    }

    if (content && type === "input") {
      htmlElement.value = content;
    }

    if (id) {
      htmlElement.id = id;
    }

    if (classes) {
      htmlElement.classList.add(...classes);
    }

    if (attributes) {
      for (const attributesKey in attributes) {
        htmlElement.setAttribute(attributesKey, attributes[attributesKey]);
      }
    }

    if (parentNode) {
      parentNode.appendChild(htmlElement);
    }

    return htmlElement;
  }

  function weatherSymbol(type) {
    let objSymbols = {
      Sunny: "&#x2600;",
      "Partly sunny": "&#x26C5;",
      Overcast: "&#x2601;",
      Rain: "&#x2614;",
      Degrees: "&#176;",
    };

    return objSymbols[type];
  }
}

attachEvents();
