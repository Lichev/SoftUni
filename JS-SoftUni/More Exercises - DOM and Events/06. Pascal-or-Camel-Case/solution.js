function solve() {
  let text = document.getElementById("text").value;
  let convention = document.getElementById("naming-convention").value;
  let print = document.getElementById("result");

  if (convention === "Camel Case") {
    camelHandler(text);
  } else if (convention === "Pascal Case") {
    pascalHandler(text);
  } else {
    print.textContent = "Error!";
  }
  function camelHandler(text) {
    let info = text.toLowerCase().split(" ");
    let result = [info[0]];
    info.slice(1).forEach((word) => {
      result.push(word[0].toUpperCase() + word.slice(1));
    });

    print.textContent = result.join("");
  }

  function pascalHandler(text) {
    let result = [];
    let info = text.toLowerCase().split(" ");
    info.forEach((word) => {
      result.push(word[0].toUpperCase() + word.slice(1));
    });

    print.textContent = result.join("");
  }
}
