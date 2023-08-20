function solve() {
  let [generateTextArea, buyTextArea] = Array.from(
    document.getElementsByTagName("textarea")
  );
  let [generateBtn, buyBtn] = Array.from(
    document.getElementsByTagName("button")
  );
  let tbody = document.querySelector(".table > tbody");
  generateBtn.addEventListener("click", generateHandler);
  buyBtn.addEventListener("click", buyHandler);

  function generateHandler() {
    const data = JSON.parse(generateTextArea.value);

    for (const { img, name, price, decFactor } of data) {
      const tableRow = createElement("tr", "", tbody);

      const firstColumn = createElement("td", "", tableRow);
      const htmlImg = createElement("img", "", firstColumn, "", "", {
        src: img,
      });

      const secondColumn = createElement("td", "", tableRow);
      const paragraphSecond = createElement("p", name, secondColumn);

      const thirdColumn = createElement("td", "", tableRow);
      const paragraphThird = createElement("p", price, thirdColumn);

      const fourthColumn = createElement("td", "", tableRow);
      const paragrahpFourth = createElement("p", decFactor, fourthColumn);

      const fifthColumn = createElement("td", "", tableRow);
      const check = createElement("input", "", fifthColumn, "", "", {
        type: "checkbox",
      });
    }
  }

  function buyHandler() {
    const tbodyChildrens = tbody.querySelectorAll("tr");

    let names = [];
    let total = 0.0;
    let factor = 0.0;

    for (const el of tbodyChildrens) {
      const info = Array.from(el.querySelectorAll("td > *"));

      if (info[4].checked) {
        names.push(info[1].textContent);
        total += Number(info[2].textContent);
        factor += Number(info[3].textContent);
      }
    }
    buyTextArea.textContent = `Bought furniture: ${names.join(', ')}\nTotal price: ${total.toFixed(2)}\nAverage decoration factor: ${ (factor/names.length) }`
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

}


