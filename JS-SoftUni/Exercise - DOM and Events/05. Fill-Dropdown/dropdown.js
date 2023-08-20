function addItem() {
  let txt = document.getElementById("newItemText");
  let value = document.getElementById("newItemValue");
  let option = document.createElement("option");
  let selection = document.getElementById("menu");
  option.setAttribute("value", value.value);
  option.textContent = txt.value
  selection.appendChild(option);
  txt.value = "";
  value.value = "";
}
