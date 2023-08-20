window.addEventListener("load", solve);

  function solve() {
    //! First section
    let genre = document.getElementById("genre");
    let name = document.getElementById("name");
    let author = document.getElementById("author");
    let date = document.getElementById("date");
    let addBtn = document.getElementById("add-btn");
    addBtn.addEventListener("click", addHandler);

    //! Second section
    let allHitsContainer = document.querySelector(".all-hits-container");

    //! Likes section
    let totalLikes = document.querySelector('.likes > p')

    //! Saved section
    let savedContainer = document.querySelector('.saved-container');



    function addHandler(event) {
    event.preventDefault();

    if (genre.value && name.value && author.value && date.value) {
      let divHitsContainer = createHitsInfo(
        genre.value,
        name.value,
        author.value,
        date.value
      );
      allHitsContainer.appendChild(divHitsContainer);
    }
  }


  //? Creation of song div container in collection of songs
  function createHitsInfo(genre, name, author, date) {
    let div = document.createElement("div");
    div.setAttribute("class", "hits-info");

    let img = document.createElement("img");
    img.setAttribute("src", "./static/img/img.png");
    div.appendChild(img);

    let genreH2 = createElement('h2', `Genre: ${genre}`, div);
    let nameH2 = createElement('h2', `Name: ${name}`, div);
    let authorH2 = createElement('h2', `Author: ${author}`, div)
    let daterH2 = createElement('h3', `Date: ${date}`, div)

    let saveBtn = createElement('button', 'Save song', div, '', ['save-btn']);
    let likeBtn = createElement('button', 'Like song', div, '', ['like-btn']);
    let deleteBtn = createElement('button', 'Delete', div, '', ['delete-btn']);


    likeBtn.addEventListener('click', likeHandler);
    saveBtn.addEventListener('click', saveHandler);
    deleteBtn.addEventListener('click', deleteHandler)

    return div;
  }



  //? Delete handler (btn inside createHitsInfo)
  function deleteHandler(event){
    event.preventDefault();
    let current = event.currentTarget;
    let parent = current.parentNode;
    let grandParent = parent.parentNode;
    grandParent.removeChild(parent);

  }


  //? Save handler (btn inside createHitsInfo)
  function saveHandler(event){
    event.preventDefault();
    let current = event.currentTarget;
    let parent = current.parentNode;
    let grandParent = parent.parentNode;
    let saveBtn = parent.querySelector('.save-btn')
    let likeBtn = parent.querySelector('.like-btn')
    parent.removeChild(saveBtn);
    parent.removeChild(likeBtn);

    grandParent.removeChild(parent);
    savedContainer.appendChild(parent);

  }


  //? Like handler (btn inside createHitsInfo)
  function  likeHandler(event){
    event.preventDefault();

    let text = totalLikes.textContent
    let textOfLikes = Array.from(text.split(': '));
    let number = Number(textOfLikes[1]) + 1;
    totalLikes.textContent = `${textOfLikes[0]}: ${number}`;
    event.target.disabled = true;

  }


  // create dom element helper:
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
