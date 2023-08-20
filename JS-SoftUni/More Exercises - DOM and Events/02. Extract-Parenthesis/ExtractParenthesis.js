function extract(content) {
  const element = document.getElementById(content).textContent;
  let first = 0;
  let second = 0;
  const words = [];

    for (let i = 0; i < element.length; i++) {
        if (element[i] === '('){
            first = i
        }else if (element[i] === ')'){
            second = i;
            words.push(element.slice(first + 1, second));
        }
    }

    console.log(words.join("; "));
}
