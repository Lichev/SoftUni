function toggle() {
  let btn = document.querySelector(".button");
  let txt = document.querySelector("#extra");

    if (btn.textContent === "More") {
      btn.textContent = "Less";
      txt.setAttribute("style", "display: block");
    } else {
      btn.textContent = "More";
      txt.setAttribute("style", "display: none");
    }
}
