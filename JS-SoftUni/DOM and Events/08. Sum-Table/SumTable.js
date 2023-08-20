function sumTable() {
  let lst = document.querySelectorAll("td:nth-child(even)");
  let result = 0;
  for (const td of lst) {
    result += Number(td.textContent);
  }
  let log = document.getElementById("sum");
  log.textContent = result;
}
