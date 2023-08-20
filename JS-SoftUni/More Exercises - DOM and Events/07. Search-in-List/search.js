function search() {
  let li = Array.from(document.querySelectorAll("li"));
  let input = document.getElementById("searchText");
  let result = document.getElementById("result");
  let count = 0;
  li.forEach((word) => {
    word.style.fontWeight = "normal";
    word.style.textDecoration = "none";
  });

  li.forEach((word) => {
    if (word.textContent.includes(input.value)) {
      count += 1;
      word.style.fontWeight = "bold";
      word.style.textDecoration = "underline";
    }
  });

  result.textContent = `${count} matches found`;
}
