window.addEventListener("load", solve);

function solve() {
  //! Repair form:
  let typeOfProduct = document.getElementById("type-product");
  let descriptionOfTheProblem = document.getElementById("description");
  let clientName = document.getElementById("client-name");
  let clientPhone = document.getElementById("client-phone");
  let sendFormBtn = document.querySelector("#right > form > button");
  sendFormBtn.addEventListener("click", sendHandler);


  //! Received orders:
    let receivedOrders = document.getElementById('received-orders');

    //! Completed orders:
    let completedOrders = document.getElementById('completed-orders');
    let clearBtn = document.querySelector('.clear-btn');
    clearBtn.addEventListener('click', clearHandler);



  function clearHandler(event){
      event.preventDefault();
      let current = event.currentTarget;
      let parent = current.parentNode;
      const elements = document.querySelectorAll('#completed-orders>.container');

      parent.removeChild(elements)

      console.log(elements.length)
  }


  function sendHandler(event) {
    event.preventDefault();

    if (
      typeOfProduct.value &&
      descriptionOfTheProblem.value &&
      clientName.value &&
      clientPhone.value
    ) {
      let div = createReceivedOrders(typeOfProduct.value, clientName.value, clientPhone.value, descriptionOfTheProblem.value);
      receivedOrders.appendChild(div);
        typeOfProduct.value = '';
        descriptionOfTheProblem.value = '';
        clientName.value = '';
        clientPhone.value = '';


    }
  }



    function createReceivedOrders(type, name, phone, description){
      let divContainer = createElement('div', '', '', '', ['container']);
      let h2 = createElement('h2', `Product type for repair: ${type}`, divContainer);
      let h3 = createElement('h3', `Client information: ${name}, ${phone}`, divContainer);
      let h4 = createElement('h4', `Description of the problem: ${description}`, divContainer);
      let startBtn = createElement('button', `Start repair`, divContainer, '', ['start-btn']);
      let finishBtn = createElement('button', `Finish repair`, divContainer, '', ['finish-btn']);
      finishBtn.disabled = true;

      startBtn.addEventListener('click', startHandler);
      finishBtn.addEventListener('click', finishHandler);

      return divContainer
    }

    function finishHandler(event){
        let current = event.currentTarget;
        let parent = current.parentNode;
        let grandParent = parent.parentNode;
        let startBtn = parent.querySelector('.start-btn');
        parent.removeChild(current);
        parent.removeChild(startBtn);
        grandParent.removeChild(parent);

        completedOrders.appendChild(parent)


    }

    function startHandler(event){
      event.preventDefault();

      let current = event.currentTarget;
      let parent = current.parentNode;
      let finishBtn = parent.querySelector('.finish-btn');
      current.disabled = true;
      finishBtn.disabled = false;


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
