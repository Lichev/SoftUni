function extractText() {
  let lst = Array.from(document.querySelectorAll("li"));
  let textArea = document.querySelector("textarea");

  textArea.textContent = lst.map((el) => el.textContent).join("\n");
  console.log(lst);
}