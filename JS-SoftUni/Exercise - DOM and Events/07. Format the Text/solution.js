function solve() {
  let txt = document.getElementById("input").value.split(".");
  let output = document.getElementById('output')
  let counter = 1;

  let temp = "";
  txt.pop()
  console.log(txt);
  while (txt.length > 0){
  let p = document.createElement('p');
  let current = txt.splice(0,3).join('.') + '.';
  p.textContent = current
  output.appendChild(p)

  }
}