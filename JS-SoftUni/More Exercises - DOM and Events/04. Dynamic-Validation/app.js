function validate() {
  let input = document.getElementById("email");

  input.addEventListener("change", inputHandler);

  function inputHandler() {
    const regex = /^[a-z]+@[a-z]+\.[a-z]+$/;
    const isValid = regex.test(input.value);

    if (isValid) {
      input.removeAttribute("class");
    } else {
      input.setAttribute("class", "error");
    }
  }
}
