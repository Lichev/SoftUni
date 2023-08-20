// TODO:
function attachEvents() {
  // Form section
  let loadBtn = document.getElementById("load-board-btn");
  let title = document.getElementById("title");
  let description = document.getElementById("description");
  let createBtn = document.getElementById("create-task-btn");

  // Board section
  let toDo = document.getElementById("todo-section");
  let inProgress = document.getElementById("in-progress-section");
  let codeReview = document.getElementById("code-review-section");
  let done = document.getElementById("done-section");
  let taskLists = Array.from(document.getElementsByClassName("task-list"));

  const BASE_URL = `http://localhost:3030/jsonstore/tasks/`;

  //Buttons event listeners
  loadBtn.addEventListener("click", loadHandler);
  createBtn.addEventListener("click", createHandler);

  function createHandler(event) {
    let obj = {
      title: title.value,
      description: description.value,
      status: "ToDo",
    };

    fetch(BASE_URL, {
      method: "POST",
      "Content-type": "application/json",
      body: JSON.stringify(obj),
    })
      .then(() => {
        loadHandler();
        title.value = "";
        description.value = "";
      })
      .catch((err) => console.log(err));
  }

  function loadHandler(event) {
    taskLists.forEach((task) => (task.innerHTML = ""));

    fetch(BASE_URL)
      .then((res) => res.json())
      .then((data) => {
        Object.keys(data).forEach((key) => {
          if (data[key].status === "ToDo") {
            let toDoList = Array.from(
              toDo.getElementsByClassName("task-list")
            )[0];
            let li = createLi(
              data[key].title,
              data[key].description,
              data[key].status,
              data[key]._id
            );
            toDoList.appendChild(li);
          } else if (data[key].status === "In Progress") {
            let toDoList = Array.from(
              inProgress.getElementsByClassName("task-list")
            )[0];
            let li = createLi(
              data[key].title,
              data[key].description,
              data[key].status,
              data[key]._id
            );
            toDoList.appendChild(li);
          } else if (data[key].status === "Code Review") {
            let toDoList = Array.from(
              codeReview.getElementsByClassName("task-list")
            )[0];
            let li = createLi(
              data[key].title,
              data[key].description,
              data[key].status,
              data[key]._id
            );
            toDoList.appendChild(li);
          } else {
            let toDoList = Array.from(
              done.getElementsByClassName("task-list")
            )[0];
            let li = createLi(
              data[key].title,
              data[key].description,
              data[key].status,
              data[key]._id
            );
            toDoList.appendChild(li);
          }
        });
      })
      .catch((err) => console.log(err));
  }

  function createLi(title, description, status, id) {
    let li = document.createElement("li");
    li.setAttribute("data-id", id);
    li.className = "task";
    let h3 = document.createElement("h3");
    h3.textContent = title;
    let p = document.createElement("p");
    p.textContent = description;
    li.appendChild(h3);
    li.appendChild(p);
    li.appendChild(createButton(status));

    return li;
  }

  function createButton(status) {
    let btn = document.createElement("button");

    if (status === "ToDo") {
      btn.textContent = "Move to In Progress";
      btn.addEventListener("click", moveToProgress);
    } else if (status === "In Progress") {
      btn.textContent = "Move to Code Review";
      btn.addEventListener("click", moveToCodeReview);
    } else if (status === "Code Review") {
      btn.textContent = "Move to Done";
        btn.addEventListener("click", moveToDone);
    } else {
      btn.textContent = "Close";
        btn.addEventListener("click", close);
    }

    return btn;
  }

  function moveToProgress(event) {
    let current = event.currentTarget;
    let currentParent = current.parentNode;
    let id = currentParent.getAttribute("data-id");

    fetch(`${BASE_URL}${id}`, {
      method: "PATCH",
      "Content-type": "application/json",
      body: JSON.stringify({
        status: "In Progress",
      }),
    })
      .then(() => {
        loadHandler();
      })
      .catch((err) => console.log(err));
  }

  function moveToCodeReview(event) {
    let current = event.currentTarget;
    let currentParent = current.parentNode;
    let id = currentParent.getAttribute("data-id");

    fetch(`${BASE_URL}${id}`, {
      method: "PATCH",
      "Content-type": "application/json",
      body: JSON.stringify({
        status: "Code Review",
      }),
    })
      .then(() => {
        loadHandler();
      })
      .catch((err) => console.log(err));
  }

  function moveToDone(event){
      let current = event.currentTarget;
      let currentParent = current.parentNode;
      let id = currentParent.getAttribute("data-id");

      fetch(`${BASE_URL}${id}`, {
          method: "PATCH",
          "Content-type": "application/json",
          body: JSON.stringify({
              status: "Done",
          }),
      })
          .then(() => {
              loadHandler();
          })
          .catch((err) => console.log(err));
  }

  function close(event){
      let current = event.currentTarget;
      let currentParent = current.parentNode;
      let id = currentParent.getAttribute("data-id");

      fetch(`${BASE_URL}${id}`, {
          method: 'DELETE'
      })
          .then(() => {
              loadHandler()
          })
          .catch(err => console.log(err))
  }
}

attachEvents();
