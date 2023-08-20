function addItem() {
  let txt = document.getElementById("newItemText");
  let newEl = document.createElement("li");
  let ulList = document.querySelector("ul");
  newEl.textContent = txt.value;
  ulList.appendChild(newEl);
  txt.value = "";
}
