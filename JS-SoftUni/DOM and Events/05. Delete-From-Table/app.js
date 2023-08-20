function deleteByEmail() {
  let lst = Array.from(
    document.querySelectorAll("#customers tr td:nth-child(even)")
  );
  let email = document.querySelector("input");
  let result = document.getElementById("result");
  let foundEl = lst.find((td) => td.textContent === email.value);

  if (foundEl) {
    foundEl.parentElement.remove();
    result.textContent = "Deleted.";
  } else {
      result.textContent = 'Not found.';
  }

  email.value = "";
}
