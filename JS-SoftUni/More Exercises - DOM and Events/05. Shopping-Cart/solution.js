function solve() {
  let buttons = Array.from(document.getElementsByClassName("add-product"));
  let textarea = Array.from(document.getElementsByTagName("textarea"))[0];
  let checkout = Array.from(document.getElementsByClassName("checkout"))[0];

  let carProduct = [];
  let totalPrice = 0.0;

  for (const button of buttons) {
    button.addEventListener("click", addHandle);
  }

  checkout.addEventListener("click", checkoutHandle);

  function checkoutHandle() {
    let list = [...new Set(carProduct)];
    textarea.textContent += `You bought ${list.join(", ")} for ${totalPrice.toFixed(2)}.`;
    checkout.disabled = true;
    buttons.forEach((btn) => (btn.disabled = true));
  }

  function addHandle(e) {
    let grandparent = e.target.parentElement.parentElement;
    let productName = Array.from(
      grandparent.getElementsByClassName("product-title")
    )[0];
    let productPrice = Array.from(
      grandparent.getElementsByClassName("product-line-price")
    )[0];

    money = productPrice.textContent;
    name = productName.textContent;

    carProduct.push(productName.textContent);
    totalPrice += Number(productPrice.textContent);
    textarea.textContent += `Added ${name} for ${money} to the cart.\n`;
  }
}
