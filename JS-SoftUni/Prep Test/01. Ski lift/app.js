window.addEventListener("load", solve);

function solve() {
  //! Buy ticket section
  let firstName = document.getElementById("first-name");
  let lastName = document.getElementById("last-name");
  let peopleCount = document.getElementById("people-count");
  let fromDate = document.getElementById("from-date");
  let daysCount = document.getElementById("days-count");
  let nextstepBtn = document.getElementById("next-btn");

  nextstepBtn.addEventListener("click", nextHandler);

  let articleList = [];

  //! Ticket preview section
  let ticketInfoList = document.querySelector(".ticket-info-list");

  //! Confirm ticket
    let confirmTicket = document.querySelector('.confirm-ticket');

    //! Main page
    let mainPage = document.getElementById('main');


  function nextHandler(event) {
    event.preventDefault();

    if (
      firstName.value &&
      lastName.value &&
      peopleCount.value &&
      fromDate.value &&
      daysCount.value
    ) {
      let li = createList(
        firstName.value,
        lastName.value,
        peopleCount.value,
        fromDate.value,
        daysCount.value
      );
      ticketInfoList.appendChild(li);
      nextstepBtn.disabled = true;

      let articleObj = {
          firstName: firstName.value,
          lastName: lastName.value,
          peopleCount: peopleCount.value,
          fromDate: fromDate.value,
          daysCount: daysCount.value
      }

      articleList.push(articleObj)

        firstName.value = '';
        lastName.value = '';
        peopleCount.value = '';
        fromDate.value = '';
        daysCount.value = '';

    }
  }

  //? create list
  function createList(firstName, lastName, peopleCount, fromDate, daysCount) {
    let li = createElement("li", '', ticketInfoList, "", ["ticket"]);
    let article = createElement("article", '', li);
    createElement("h3", `Name: ${firstName} ${lastName}`, article);
    createElement("p", `From date: ${fromDate}`, article);
    createElement("p", `For ${daysCount} days`, article);
    createElement("p", `For ${peopleCount} people`, article);

    let editBtn = createElement("button", `Edit`, li, "", ["edit-btn"]);
    let continueBtn = createElement("button", `Continue`, li, "", [
      "continue-btn",
    ]);

    editBtn.addEventListener('click', editHandler);
    continueBtn.addEventListener('click', continueHandler);

    return li;
  }

  function continueHandler(event){
      event.preventDefault()

      let parent = event.currentTarget.parentNode;

      let editBtn = parent.querySelector('.edit-btn');
      let continueBtn = parent.querySelector('.continue-btn');
      let confirmBtn = createElement('button', 'Confirm', '', '', ['confirm-btn']);
      let cancelBtn = createElement('button', 'Cancel', '', '', ['cancel-btn']);
      parent.setAttribute('class', 'ticket-content');

      parent.replaceChild(confirmBtn, editBtn);
      parent.replaceChild(cancelBtn, continueBtn);

      ticketInfoList.innerHTML = '';
      confirmTicket.appendChild(parent);

      confirmBtn.addEventListener('click', confirmHandler);
      cancelBtn.addEventListener('click', cancelHandler);
  }

  function cancelHandler(){
      confirmTicket.innerHTML = ''
  }

  function confirmHandler(event){
      event.preventDefault();

      mainPage.innerHTML = ``

      createElement('h1', 'Thank you, have a nice day!', mainPage, 'thank-you')
      let backBtn = createElement('button', 'Back', mainPage, 'back-btn')

      backBtn.addEventListener('click', reload)

  }

  function reload(){
      location.reload();
  }

  function editHandler(event){
      event.preventDefault();
      let obj = articleList[0]

      firstName.value = obj.firstName;
      lastName.value = obj.lastName;
      peopleCount.value = obj.peopleCount;
      fromDate.value = obj.fromDate;
      daysCount.value = obj.daysCount;

      ticketInfoList.innerHTML = ''
      articleList.length = 0;
      nextstepBtn.disabled = false;
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
