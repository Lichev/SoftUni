function create(words) {
  for (const word of words) {
    let div = document.createElement("div");
    let p = document.createElement("p");
    let content = document.getElementById("content");
    content.appendChild(div);
    p.setAttribute("style", "display: none");
    p.textContent = word;
    div.appendChild(p);

    div.addEventListener("click", () => {
      p.setAttribute("style", "display: block");
    });
  }
}
