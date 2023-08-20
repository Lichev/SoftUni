function solution() {
  //! first section
  let input = document.querySelector(
    "body > div > section:nth-child(1) > div > input[type=text]"
  );
  let addBtn = document.querySelector(
    "body > div > section:nth-child(1) > div > button"
  );

  addBtn.addEventListener("click", addHandler);

  //! second section
  let listOfGifts = document.querySelector(
    "body > div > section:nth-child(2) > ul"
  );

  //! third section
  let sentGiftList = document.querySelector(
    "body > div > section:nth-child(3) > ul"
  );

  //! Fourth section
    let discardList = document.querySelector('body > div > section:nth-child(4) > ul');


  function addHandler() {
    if (input.value) {
      let li = createElement("li", input.value, listOfGifts, "", ["gift"]);
      let sendBtn = createElement("button", "Send", li, "sendButton");
      let discardBtn = createElement("button", "Discard", li, "discardButton");


      sendBtn.addEventListener('click', sendHandler);
      discardBtn.addEventListener('click', discardHandler);
    }
  }

  function discardHandler(event){
      let current = event.currentTarget;
      let parent = current.parentNode;
      let sndBtn = parent.querySelector('#sendButton');
      let discardBtn = parent.querySelector('#discardButton');
      listOfGifts.removeChild(parent);
      parent.removeChild(sndBtn);
      parent.removeChild(discardBtn);
      discardList.appendChild(parent);

  }


  function sendHandler(event){
      let current = event.currentTarget;
      let parent = current.parentNode;
      let sndBtn = parent.querySelector('#sendButton');
      let discardBtn = parent.querySelector('#discardButton');
      listOfGifts.removeChild(parent);
      parent.removeChild(sndBtn);
      parent.removeChild(discardBtn);
      sentGiftList.appendChild(parent);
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
