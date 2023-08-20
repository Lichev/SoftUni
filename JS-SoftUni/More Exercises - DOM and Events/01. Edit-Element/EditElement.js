function editElement(element, match, replacer) {
  const searchRegExp = new RegExp(match, "g");
  element.textContent = element.textContent.replace(searchRegExp, replacer);
}
