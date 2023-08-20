function colorize() {
    let items = Array.from(document.querySelectorAll('tr:nth-child(even)'));
    items.forEach((tr) => tr.setAttribute('style', 'background-color: teal'))
}