// TODO
function attachEvents() {
  let title = document.getElementById("title");
  let addBtn = document.getElementById("add-button");
  let loadBtn = document.getElementById("load-button");
  let BASE_URL = `http://localhost:3030/jsonstore/tasks/`;

  let toDoList = document.getElementById("todo-list");

  loadBtn.addEventListener("click", loadHandler);
  addBtn.addEventListener("click", addHandler);

  function addHandler(event) {
    event.preventDefault();
    let taskName = title.value;

    let obj = {
      name: taskName,
    };

    fetch(BASE_URL, {
      method: "POST",
      "Content-type": "application/json",
      body: JSON.stringify(obj),
    })
      .then(() => {
        loadHandler(new Event("click"));
        title.value = "";
      })
      .catch((err) => console.log(err));
  }

  function loadHandler(event) {
    event.preventDefault();
    toDoList.innerHTML = "";

    fetch(BASE_URL)
      .then((response) => response.json())
      .then((data) => {
        Object.values(data).forEach((key) => {
          let li = createLi(key.name, key._id);
          toDoList.appendChild(li);
        });
      })
      .catch((err) => console.log(err));
  }

  function createLi(name, id) {
    let li = document.createElement("li");
    li.setAttribute("data-id", id);
    let span = document.createElement("span");
    span.textContent = name;
    let removeBtn = document.createElement("button");
    let editBtn = document.createElement("button");
    removeBtn.textContent = "Remove";
    editBtn.textContent = "Edit";

    removeBtn.addEventListener("click", removeHandler);
    editBtn.addEventListener("click", editHandler)

    li.appendChild(span);
    li.appendChild(removeBtn);
    li.appendChild(editBtn);

    return li;
  }

  function removeHandler(event) {
    let current = event.currentTarget;
    let parent = current.parentNode;
    let id = parent.getAttribute('data-id')
    console.log(id);

    fetch(`${BASE_URL}${id}`, {
      method: 'DELETE',
    })
        .then(() => {
          loadHandler(new Event("click"));
        })
        .catch(err => console.log(err))
  }

  function editHandler(event){
    let current = event.currentTarget
    let parent = current.parentNode
    let id = parent.getAttribute('data-id')
    let span = parent.querySelector('span')
    let input = document.createElement('input');
    let submit = document.createElement('button');
    input.value = span.textContent;
    submit.textContent = 'Submit';

    parent.replaceChild(input, span);
    parent.replaceChild(submit, current)

    submit.addEventListener("click", submitHandler);
  }


  function submitHandler(event){
    let current = event.currentTarget
    let parent = current.parentNode
    let id = parent.getAttribute('data-id')
    let input = parent.querySelector('input');


    fetch(`${BASE_URL}${id}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name: input.value
      })
    })
        .then(() => {
          loadHandler(new Event("click"));
        })
        .catch(err => console.log(err))
  }
}

attachEvents();
