function attachEvents() {
  let phonebook = document.getElementById("phonebook");
  let btnLoad = document.getElementById("btnLoad");
  let btnCreate = document.getElementById("btnCreate");
  let person = document.getElementById("person");
  let phone = document.getElementById("phone");
  let BASE_URL = "http://localhost:3030/jsonstore/phonebook/";

  btnLoad.addEventListener("click", btnLoadHandler);
  btnCreate.addEventListener("click", btnCreateHandler);

  function btnLoadHandler() {
    phonebook.innerHTML = "";
    fetch(BASE_URL)
      .then((response) => response.json())
      .then((data) => {
        const lstData = Object.values(data);
        lstData.forEach((phone) => {
          const content = `${phone.person}: ${phone.phone}`;
          const li = createElement("li", content, phonebook);
          li.setAttribute("data-id", phone["_id"]);
          let deleteBtn = createElement("button", "Delete", li);
          deleteBtn.addEventListener("click", () => deleteBtnHandler);
        });
      });
  }

  function deleteBtnHandler(e) {
    const deleteBtn = e.currentTarget;
    const parent = deleteBtn.parentNode;
    const key = parent.getAttribute("data-id");
    parent.remove();
    console.log(key);

    return fetch(BASE_URL + key, {
      method: "DELETE",
    }).then((response) => response.json());
  }

  function btnCreateHandler() {
    const obj = {
      person: person.value,
      phone: phone.value,
    };

    fetch(BASE_URL, {
      method: "POST",
      body: JSON.stringify(obj),
      headers: {
        "Content-Type": "application/json",
      },
    }).then((response) => response.json())
        .then(data => console.log(data))
        .catch(err => console.log(err));
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

attachEvents();
