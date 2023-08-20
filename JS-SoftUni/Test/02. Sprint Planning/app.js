window.addEventListener("load", solve);

function solve() {
  let taskTitle = document.getElementById("title");
  let taskDescr = document.getElementById("description");
  let taskLabel = document.getElementById("label");
  let taksPoint = document.getElementById("points");
  let taskAssign = document.getElementById("assignee");
  let tasksSection = document.getElementById("tasks-section");
  let points = document.getElementById("total-sprint-points");
  let form = document.getElementById('create-task-form')

  let taskId = document.getElementById('task-id');

  let createBtn = document.getElementById("create-task-btn");
  let deleteBtn = document.getElementById("delete-task-btn");

  let tasksID = 0;
  let totalPoints = 0;

  createBtn.addEventListener("click", createHandler);
  deleteBtn.addEventListener("click", deleteHandler);


  function deleteHandler(e){
    let current = e.currentTarget;
    let articleID = taskId.textContent
    const deleteArticle = document.getElementById(articleID)
    const pointsCurrent = deleteArticle.getElementsByClassName('task-card-points')[0];
    const regex = /\d+(\.\d+)?/g;
    let newPoints = pointsCurrent.textContent.match(regex)[0];
    deleteArticle.remove()

    taskTitle.value = "";
    taskDescr.value = "";
    taskLabel.value = "";
    taksPoint.value = "";
    taskAssign.value = "";

    createBtn.disabled = false;
    deleteBtn.disabled = true;
    taskTitle.disabled = false;
    taskDescr.disabled = false;
    taskLabel.disabled = false;
    taksPoint.disabled = false;
    taskAssign.disabled = false;
    totalPoints -= Number(newPoints)
    points.innerText = `Total Points ${totalPoints}pts`;
    taskId.textContent = ''

  }


  function createHandler() {
    // console.log(taskTitle.value, taskDescr.value, taskLabel.value, taksPoint.value, taskAssign.value);
    if (
        taskTitle.value !== "" &&
        taskDescr.value !== "" &&
        taskLabel.value !== "" &&
        taksPoint.value !== "" &&
        taskAssign.value !== ""
    ) {
      tasksID += 1;
      totalPoints += Number(taksPoint.value);
      let article = createElement(
          "article",
          "",
          tasksSection,
          `task-${tasksID}`,
          ["task-card"]
      );
      points.innerText = `Total Points ${totalPoints}pts`;
      let typeLabel = cardLabel(taskLabel.value);
      let iconLabel = cardLabelIcont(taskLabel.value);
      let taskCardLabel = createElement("div", "", article, "", [
        "task-card-label",
        `${typeLabel}`,
      ]);
      taskCardLabel.innerHTML = `${taskLabel.value} ${iconLabel}`;
      let h3 = createElement("h3", taskTitle.value, article, "", [
        "task-card-title",
      ]);
      let p = createElement("p", taskDescr.value, article, "", [
        "task-card-description",
      ]);
      let taskCardPoints = createElement(
          "div",
          `Estimated at ${taksPoint.value} pts`,
          article,
          "",
          ["task-card-points"]
      );
      let taskCardAssignee = createElement(
          "div",
          `Assigned to: ${taskAssign.value}`,
          article,
          "",
          ["task-card-assignee"]
      );
      let taskCardAction = createElement("div", "", article, "", [
        "task-card-actions",
      ]);
      let deleteArticleBtn = createElement("button", "Delete", taskCardAction);

      deleteArticleBtn.addEventListener("click", deleteArticleHandler);

      taskTitle.value = "";
      taskDescr.value = "";
      taskLabel.value = "";
      taksPoint.value = "";
      taskAssign.value = "";
    }
  }

  function deleteArticleHandler(e) {
    let current = e.currentTarget;
    let [label, title, description, points, assignee] =
        current.parentNode.parentNode.children;
    const regex = /\d+(\.\d+)?/g;
    points = points.textContent.match(regex)[0];
    let newLabel = label.textContent;
    let newAssigne = assignee.textContent
    let id = current.parentNode.parentNode
    console.log(id.getAttribute("id"))



    taskTitle.value = title.textContent;
    taskDescr.value = description.textContent;
    taskLabel.value = newLabel.split(' ')[0];
    taksPoint.value = points;
    taskAssign.value = assignee.textContent.split(': ')[1];
    createBtn.disabled = true;
    deleteBtn.disabled = false;
    taskTitle.disabled = true;
    taskDescr.disabled = true;
    taskLabel.disabled = true;
    taksPoint.disabled = true;
    taskAssign.disabled = true;
    taskId.textContent = id.getAttribute("id")
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

  function cardLabel(label) {
    if (label === "Feature") {
      return `feature`;
    } else if (label === "Low Priority Bug") {
      return "low-priority";
    } else {
      return "high-priority";
    }
  }

  function cardLabelIcont(label) {
    if (label === "Feature") {
      return `&#8865`;
    } else if (label === "Low Priority Bug") {
      return "&#9737";
    } else {
      return "&#9888";
    }
  }
}