function lockedProfile() {
    let main = document.getElementById('main');
    let BASE_URL = `http://localhost:3030/jsonstore/advanced/profiles/`;
    main.innerHTML = '';



    fetch(BASE_URL)
        .then(res => res.json())
        .then((data) => {
            Object.keys(data).forEach(key => {
                createProfileContainer(data[key]._id, data[key].username, data[key].email, data[key].age)
            })
        })
        .catch(err => console.log(err))


    function createProfileContainer(id, username, email, age){
      let divProfile = createElement('div', '', main, '', ['profile']);
      let imgProfile = document.createElement('img');
      imgProfile.setAttribute('src', './iconProfile2.png');
      imgProfile.setAttribute('class', 'userIcon');
      divProfile.appendChild(imgProfile);

      createElement('label', 'Lock', divProfile);
      let lock = createElement('input', '', divProfile, '', '', {type: 'radio', name: id, value: 'lock', checked: ''});
      createElement('label', 'Unlock', divProfile);
      let unlock = createElement('input', '', divProfile, '', '', {type: 'radio', name: id, value: 'unlock'});
      createElement('br', '', divProfile);
      createElement('hr', '', divProfile);
      createElement('label', 'Username', divProfile);
      let name =  createElement('input', '', divProfile, '', '', {type: 'text', name: id, value: username});
      name.disabled = true;
      name.readOnly = true;

      let divHidden = createElement('div', '', divProfile, id, ['hiddenInfo']);
      createElement('hr', '', divHidden);
      createElement('label', 'Email:', divHidden);
      let userMail = createElement('input', '', divHidden, '', '', {type: 'email', name: id, value: email});
      userMail.disabled = true;
      userMail.readOnly = true;
      createElement('label', 'Age:', divHidden);
      let userAge = createElement('input', '', divHidden, '', '', {type: 'email', name: id, value: age});
      userAge.disabled = true;
      userAge.readOnly = true;

      let showMore = createElement('button', 'Show More', divProfile);

      showMore.addEventListener('click', showHandler);

      return divProfile;

    }


    function showHandler(event){
        event.preventDefault()
        let current = event.currentTarget
        let parent = event.currentTarget.parentNode;
        let lock = Array.from(parent.querySelectorAll('input[type=radio]'))

        if (!lock[0].checked) {
            const elements = parent.querySelectorAll('.hiddenInfo > input, .hiddenInfo > label');
            console.log(elements)
            elements.forEach(element => {
                element.style.display = 'block';
            });

            let hideBtn = document.createElement('button');
            hideBtn.textContent = 'Hide it';
            parent.replaceChild(hideBtn, current)

            hideBtn.addEventListener('click', hideHandler)
        }


    }


    function hideHandler(event){
        let current = event.currentTarget
        let parent = event.currentTarget.parentNode;
        let lock = Array.from(parent.querySelectorAll('input[type=radio]'))

        if (!lock[0].checked) {
            const elements = parent.querySelectorAll('.hiddenInfo > input, .hiddenInfo > label');
            console.log(elements)
            elements.forEach(element => {
                element.style.display = 'none';
            });

            let showMore = document.createElement('button');
            showMore.textContent = 'Show more';
            showMore.addEventListener("click", showHandler)

            parent.replaceChild(showMore, current)
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