function focused() {
  let input = Array.from(document.querySelectorAll('input'));

  for (const element of input) {
    element.addEventListener('focus', () => {
      element.parentElement.setAttribute('class', 'focused')
    })

    element.addEventListener("blur", () => {
      element.parentElement.removeAttribute('class')
    })
  }
}