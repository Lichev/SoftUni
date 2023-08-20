window.addEventListener("load", solve);

function solve() {
    let BASE_URL = `http://localhost:3030/jsonstore/tasks/`;

    let courseName = document.getElementById('course-name');
    let courseType = document.getElementById('course-type');
    let description = document.getElementById('description');
    let teacherName = document.getElementById('teacher-name');


    let loadBtn = document.getElementById('load-course');
    let divList = document.getElementById('list');


    let editCourseBtn = document.getElementById('edit-course');
    let addCourseBtn = document.getElementById('add-course');

    loadBtn.addEventListener('click', loadHandler)
    addCourseBtn.addEventListener('click', addHandler)
    editCourseBtn.addEventListener('click', editFetchHandler)

    function editFetchHandler(event){
        event.preventDefault();
        let id = courseName.getAttribute('data-id')
        console.log(id)
        if (courseName.value &&  courseType.value &&  description.value &&  teacherName.value){
            if (courseType.value === 'Long' || courseType.value === 'Medium' || courseType.value === 'Short'){
                let obj = {
                    title: courseName.value,
                    type: courseType.value,
                    description: description.value,
                    teacher: teacherName.value,
                    _id: id
                }

                fetch(`${BASE_URL}${id}`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(obj),
                })
                    .then(() => {
                        loadHandler(new Event("click"));
                        courseName.removeAttribute('data-id')
                    })
                    .catch(err => console.log(err))
            }
        }
    }



    function loadHandler(event){
        event.preventDefault()

        editCourseBtn.disabled = true;
        addCourseBtn.disabled = false;
        divList.innerHTML = '';

        fetch(BASE_URL)
            .then(res => res.json())
            .then(data => {
                Object.values(data).forEach(key => {
                    let div = createDivContainer(key.title, key.type, key.description, key.teacher, key._id);
                    divList.appendChild(div);
                })
            })
            .catch(err => console.log(err))

    }


    function addHandler(event){
        event.preventDefault()

        if (courseName.value &&  courseType.value &&  description.value &&  teacherName.value){
            if (courseType.value === 'Long' || courseType.value === 'Medium' || courseType.value === 'Short'){
                let obj = {
                    title: courseName.value,
                    type: courseType.value,
                    description: description.value,
                    teacher: teacherName.value
                }

                fetch(BASE_URL, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(obj),
                })
                    .then(() => {
                        loadHandler(new Event("click"));
                        courseName.value = '';
                        courseType.value = '';
                        description.value = '';
                        teacherName.value = '';
                    })
                    .catch(err => console.log(err))

            }
        }


    }

    function createDivContainer(title, type, description, teacher, id){
        let div = createElement('div', '', '', '', ['container']);
        let titleH2 = createElement('h2', title, div);
        let teacherH3 = createElement('h3', teacher, div);
        let typeH3 = createElement('h3', type, div);
        let descriptionH4 = createElement('h4', description, div);
        div.setAttribute('data-id', id)

        let editBtn = createElement('button', 'Edit Course', div, '', ['edit-btn']);
        let finishBtn = createElement('button', 'Finish Course', div, '',['finish-btn']);

        editBtn.addEventListener('click', editHandler);
        finishBtn.addEventListener('click', finishHandler);

        return div
    }

    function finishHandler(event){
        event.preventDefault()
        let current = event.currentTarget
        let parent = current.parentNode;
        let id = parent.getAttribute('data-id')
        console.log(id);

        fetch(`${BASE_URL}${id}`, {
            method: "Delete",
        })
            .then(() => {
                loadHandler(new Event("click"));
            })
            .catch((err) => console.log(err));

    }

    function editHandler(event){
        event.preventDefault();
        let current = event.currentTarget
        let parent = current.parentNode;
        let id = parent.getAttribute('data-id')


        let title = parent.querySelector('h2').textContent;
        let teacher = parent.querySelector('h3:nth-child(2)').textContent;
        let type = parent.querySelector('h3:nth-child(3)').textContent;
        let descr = parent.querySelector('h4').textContent;

        courseName.value = title;
        courseType.value = type;
        description.value = descr;
        teacherName.value = teacher;
        courseName.setAttribute('data-id', id)

        divList.removeChild(parent);
        addCourseBtn.disabled = true;
        editCourseBtn.disabled = false;

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