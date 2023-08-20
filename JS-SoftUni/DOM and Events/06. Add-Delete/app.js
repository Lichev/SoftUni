function addItem() {
  let txt = document.getElementById("newItemText");
  let newEl = document.createElement("li");
  let ulList = document.querySelector("ul");
  let a = document.createElement("a");
  a.setAttribute("href", "#");
  newEl.textContent = txt.value;
  ulList.appendChild(newEl);
  a.textContent = "[Delete]";
  newEl.appendChild(a);
  a.addEventListener("click", deleteHandler);
  txt.value = "";

  function deleteHandler(e){
      let anchor = e.currentTarget
      anchor.parentElement.remove();
  }
}
