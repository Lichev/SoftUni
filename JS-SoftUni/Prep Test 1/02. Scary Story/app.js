window.addEventListener("load", solve);

function solve() {
  const main = document.getElementById('main')

  // Left side
  const firstName = document.getElementById("first-name");
  const lastName = document.getElementById("last-name");
  const age = document.getElementById("age");
  const storyTitle = document.getElementById("story-title");
  const genre = document.getElementById("genre");
  const yourStory = document.getElementById("story");
  const publishBtn = document.getElementById("form-btn");


  // Rights side
  const previewList = document.getElementById("preview-list");
  const saveBtn = createElement('button', 'Save Story', '', '', ['save-btn']);
  const editBtn = createElement('button', 'Edit Story', '', '', ['edit-btn']);
  const deleteBtn = createElement('button', 'Delete Story', '', '', ['delete-btn']);
  const li = createElement("li", "", '', "", [`story-info`]);
  const article = createElement("article", "");
  const h4 = createElement("h4", "");
  const pAge = createElement("p", "", );
  const pTitle = createElement('p', '');
  const pGenre = createElement('p', '');
  const pStory = createElement('p', ``);


  publishBtn.addEventListener("click", publishHandler);
  editBtn.addEventListener('click', editHandler);
  deleteBtn.addEventListener('click', deleteHandler);
  saveBtn.addEventListener('click', saveHandler);

  function saveHandler(){
    main.innerHTML = '<h1>Your story is saved!</h1>'
  }
  
  function deleteHandler(){
    publishBtn.disabled = false;
    previewList.innerHTML = '<h3>Preview</h3>';
  }

  function editHandler(){
    let [_name, first, last] = h4.textContent.split(" ");
    let [_age, numAge] = pAge.textContent.split(" ");
    let [_title, nameTitle] = pTitle.textContent.split(" ");

    firstName.value = first;
    lastName.value = last;
    age.value = Number(numAge);
    storyTitle.value = nameTitle;
    yourStory.value = pStory.textContent

    publishBtn.disabled = false;

    previewList.innerHTML = '<h3>Preview</h3>';
  }

  function publishHandler(e) {
    if (
      firstName.value !== "" &&
      lastName.value !== "" &&
      age.value !== "" &&
      storyTitle.value !== "" &&
      genre.value !== "" &&
      yourStory.value !== ""
    ) {
      const current = e.currentTarget;
      previewList.appendChild(li);
      li.appendChild(article);
      article.appendChild(h4);
      article.appendChild(pAge);
      article.appendChild(pTitle)
      article.appendChild(pGenre)
      article.appendChild(pStory)

      h4.innerText = `Name: ${firstName.value} ${lastName.value}`;
      pAge.innerText = `Age: ${age.value}`;
      pTitle.innerText = `Title: ${storyTitle.value}`;
      pGenre.innerText = `Genre: ${genre.value}`;
      pStory.innerText = `${yourStory.value}`

      li.appendChild(saveBtn);
      li.appendChild(editBtn);
      li.appendChild(deleteBtn);
      current.disabled = true;
      firstName.value = '';
      lastName.value = '';
      age.value = '';
      storyTitle.value = '';
      yourStory.value = '';

    }
  }

  function createElement(type, content, parentNode, id, classes, attributes) {
    const htmlElement = document.createElement(type);

    if (content && type !== "input") {
      htmlElement.textContent = content;
    }

    if (content && type === "input") {
      htmlElement.value = content;
    }

    if (id) {
      htmlElement.id = id;
    }

    if (classes) {
      htmlElement.classList.add(...classes);
    }

    if (attributes) {
      for (const attributesKey in attributes) {
        htmlElement.setAttribute(attributesKey, attributes[attributesKey]);
      }
    }

    if (parentNode) {
      parentNode.appendChild(htmlElement);
    }

    return htmlElement;
  }
}
