window.addEventListener('load', solution)

function solution() {
   let main = document.getElementById('main');
   let articleList_URL = `http://localhost:3030/jsonstore/advanced/articles/list`
   let infoUrl = `http://localhost:3030/jsonstore/advanced/articles/details/`

   fetch(articleList_URL)
       .then(res => res.json())
       .then(data => {
          Object.keys(data).forEach(key => {
             createArticle(data[key]._id, data[key].title)
          })
       })
       .catch(err => console.log(err))

   function createArticle(id, title){
      let mainDiv = createElement('div', '', main, '', ['accordion']);
      let headDiv = createElement('div', '', mainDiv, '', ['head']);
      let span = createElement('span', title, headDiv);
      let moreBtn = createElement('button', 'More', headDiv, id, ['button'])

      let extraDiv = createElement('div', '', mainDiv, '', ['extra']);
      let p = createElement('p', '', extraDiv);
      extraDiv.style.display = 'none';

      moreBtn.addEventListener('click', moreHandler)
   }

   function moreHandler(event){
      event.preventDefault();
      let current = event.currentTarget;
      let id = current.getAttribute('id');
      let mainDiv = current.parentNode.parentNode;
      let extra = mainDiv.querySelector('.extra');
      let p = mainDiv.querySelector('.extra > p');
      let head = current.parentNode;

      let lessBtn = document.createElement('button');
      lessBtn.textContent = 'Less';
      lessBtn.setAttribute('id', id)
      lessBtn.setAttribute('class', 'button')
      lessBtn.addEventListener('click', lessHandler)

      fetch(`${infoUrl}${id}`)
          .then(res => res.json())
          .then(data => {
             p.textContent = data.content;
             extra.style.display = 'block';
            head.replaceChild(lessBtn, current)

          })
          .catch(err => console.log(err))
   }

   function lessHandler(event){
      event.preventDefault();
      let current = event.currentTarget;
      let id = current.getAttribute('id');
      let mainDiv = current.parentNode.parentNode;
      let extra = mainDiv.querySelector('.extra');
      let p = mainDiv.querySelector('.extra > p');
      let head = current.parentNode;

      let moreBtn = document.createElement('button');
      moreBtn.textContent = 'More';
      moreBtn.setAttribute('id', id)
      moreBtn.setAttribute('class', 'button')
      moreBtn.addEventListener('click', moreHandler)


      extra.style.display = 'none';
      head.replaceChild(moreBtn, current);
   }


   //? create dom element helper:
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