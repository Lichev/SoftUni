function solve() {
  document.querySelector("#searchBtn").addEventListener("click", onClick);
  let rows = Array.from(document.querySelectorAll("tr"));
  function onClick() {
    rows.forEach((el) => {
      el.removeAttribute("class");
    });

    let info = document.querySelector('input[type="text"]');
    let td = Array.from(document.querySelectorAll("td"));

    for (const tdEl of td) {
      if (tdEl.textContent.includes(info.value)) {
        let parent = tdEl.parentNode;
        parent.setAttribute("class", "select");
      }
    }
    info.value = "";
  }
}
