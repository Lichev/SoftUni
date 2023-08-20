window.addEventListener("load", solve);

function solve() {
  //! Load and create
  let BASE_URL = `http://localhost:3030/jsonstore/grocery/`;
  let loadBtn = document.getElementById("load-product");
  let tbody = document.getElementById("tbody");

  //! Add
  let productName = document.getElementById("product");
  let count = document.getElementById("count");
  let price = document.getElementById("price");
  let addBtn = document.getElementById("add-product");

  //! Update
  let updateProductBtn = document.getElementById("update-product");
  let updateElement = [];

  //! Btn listeners
  loadBtn.addEventListener("click", loadHandler);
  addBtn.addEventListener("click", addHandler);
  updateProductBtn.addEventListener("click", mainUpdateHandler);

  function mainUpdateHandler(event) {
    event.preventDefault();
    let id = updateElement[0].getAttribute("data-id");
    let obj = {
      product: productName.value,
      count: count.value,
      price: price.value,
    };

    if (productName.value && count.value && price.value) {
      fetch(`${BASE_URL}${id}`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(obj),
      })
        .then(() => {
          loadHandler(new Event("click"));
            productName.value = '';
            count.value = '';
            price.value = '';
            addBtn.disabled = false;
            updateProductBtn.disabled = true;

        })
        .catch((err) => console.log(err));
    }
  }

  function addHandler(event) {
    event.preventDefault();

    if (productName.value && count.value && price.value) {
      let obj = {
        product: productName.value,
        count: count.value,
        price: price.value,
      };

      fetch(BASE_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(obj),
      })
        .then(() => {
          loadHandler(new Event("click"));
            productName.value = '';
            count.value = '';
            price.value = '';

        })
        .catch((err) => console.log(err));
    }
  }

  function loadHandler(event) {
    event.preventDefault();

    tbody.innerHTML = "";
    fetch(BASE_URL)
      .then((res) => res.json())
      .then((data) => {
        Object.values(data).forEach((key) => {
          let tableRol = createTr(key.product, key.count, key.price, key._id);
          tbody.appendChild(tableRol);
        });
      })
      .catch((err) => console.log(err));
  }

  //? Create table body children
  function createTr(name, count, price, id) {
    let tr = document.createElement("tr");
    tr.setAttribute("data-id", id);
    createElement("td", name, tr, "", ["name"]);
    createElement("td", count, tr, "", ["count-product"]);
    createElement("td", price, tr, "", ["product-price"]);

    let btn = createElement("td", "", tr, "", ["btn"]);
    let updateBtn = createElement("button", "Update", btn, "", ["update"]);
    let deleteBtn = createElement("button", "Delete", btn, "", ["delete"]);

    deleteBtn.addEventListener("click", deleteHandler);
    updateBtn.addEventListener("click", updateHandler);

    return tr;
  }

  function updateHandler(event) {
    event.preventDefault();

    let parent = event.currentTarget.parentNode.parentNode;
    let n = parent.querySelector(".name").textContent;
    let c = parent.querySelector(".count-product").textContent;
    let p = parent.querySelector(".product-price").textContent;

    productName.value = n;
    count.value = c;
    price.value = p;

    addBtn.disabled = true;
    updateProductBtn.disabled = false;

    updateElement.push(parent);
  }

  function deleteHandler(event) {
    event.preventDefault();
    let parent = event.currentTarget.parentNode.parentNode;
    let id = parent.getAttribute("data-id");

    fetch(`${BASE_URL}${id}`, {
      method: "Delete",
    })
      .then(() => {
        loadHandler(new Event("click"));
      })
      .catch((err) => console.log(err));
  }

  //? create dom element helper:
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
