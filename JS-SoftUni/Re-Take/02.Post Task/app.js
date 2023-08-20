window.addEventListener("load", solve);

function solve() {
  let taskTitle = document.getElementById('task-title');
  let taskCategory = document.getElementById('task-category');
  let taskContent = document.getElementById('task-content');
  let publishBtn = document.getElementById('publish-btn');


  let reviewList = document.getElementById('review-list');

  let publishedList = document.getElementById('published-list');


  publishBtn.addEventListener('click', publishHandler);

  function publishHandler(){

    if (taskTitle.value && taskCategory.value && taskContent.value) {
        let li = createElement('li', '', reviewList, '', ['rpost'])
        let article = createElement('article', '', li);
        let h4 = createElement('h4', taskTitle.value, article);
        let cat = createElement('p', `Category: ${taskCategory.value}`, article);
        let content = createElement('p', `Content: ${taskContent.value}`, article);

        let editBtn = createElement('button', `Edit`, li, '', ['action-btn', 'edit'])
        let postBtn = createElement('button', 'Post', li, '', ['action-btn', 'post'])
        taskTitle.value = '';
        taskCategory.value = '';
        taskContent.value = '';

        editBtn.addEventListener('click', editHandler)
        postBtn.addEventListener('click', postHandler)

      }

    function postHandler(event){
        event.preventDefault()
        let current = event.currentTarget
        let parent = current.parentNode;
        let editBtn = parent.querySelector('.edit');
        let postBtn = parent.querySelector('.post');

        parent.removeChild(editBtn);
        parent.removeChild(postBtn);

        reviewList.removeChild(parent);
        publishedList.appendChild(parent);


    }

    function editHandler(event){
        event.preventDefault()
        let current = event.currentTarget
        let parent = current.parentNode;
        let title = parent.querySelector('article > h4').textContent
        let cat = Array.from(parent.querySelector('article > p:nth-child(2)').textContent.split(': '))[1];
        let content = Array.from(parent.querySelector('article > p:nth-child(3)').textContent.split(': '))[1];

        taskTitle.value = title;
        taskCategory.value = cat;
        taskContent.value = content;

        reviewList.removeChild(parent)
    }
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