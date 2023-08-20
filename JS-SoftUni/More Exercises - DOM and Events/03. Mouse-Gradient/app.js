function attachGradientEvents() {
  const element = document.getElementById("gradient");
  const result = document.getElementById("result");

    element.addEventListener("mousemove", (e) => {
    const x = e.offsetX;
    const width = element.clientWidth;
    const percentage = Math.floor((x / width) * 100);

    result.textContent = `${percentage}%`;
  });
}
