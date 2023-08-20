function lockedProfile() {
  let parents = Array.from(document.querySelectorAll(".profile"));

  for (let parent of parents) {
    let button = parent.querySelector("button");
    let lock = parent.querySelector('input[value="lock"]');
    let unlock = parent.querySelector('input[value="unlock"]');
    let hidden = parent.querySelector("div");

    lock.addEventListener("click", () => {
      lock.checked = true;
      unlock.checked = false;
      button.disabled = true;
      console.log(unlock.checked);
      console.log(lock.checked);
    });

    unlock.addEventListener("click", () => {
      unlock.checked = true;
      lock.checked = false;
      button.disabled = false;
      console.log(unlock.checked);
      console.log(lock.checked);
    });

    button.addEventListener("click", () => {
      if (button.textContent === "Show more") {
        if (lock.checked) {
        } else if (unlock.checked) {
          hidden.setAttribute("style", "display: block");
          button.textContent = "Hide it";
        }
      } else if (button.textContent === "Hide it") {
        if (lock.checked) {
        } else if (unlock.checked) {
          hidden.setAttribute("style", "display: none");
          button.textContent = "Show more";
        }
      }
    });
  }
}
