function solve(arr) {
  const num = Number(arr[0]);
  const people = arr.slice(1, num + 1);
  const rest = arr.slice(num + 1);

  let taskObjects = people.map((task) => {
    const [assignee, taskId, title, status, estimatedPoints] = task.split(":");
    return { assignee, taskId, title, status, estimatedPoints };
  });

  for (const restElement of rest) {
    const [command, assignee, taskId, title, status, estimatedPoints] =
      restElement.split(":");

    if (command === "Add New") {
      addNewTask(assignee, taskId, title, status, estimatedPoints);
    } else if (command === "Change Status") {
      changeTaskStatus(assignee, taskId, title);
    } else if (command === "Remove Task") {
      removeTask(assignee, taskId);
    }
  }

  let toDo = 0;
  let inProgess = 0;
  let codeReview = 0;
  let donePoints = 0;

  for (const element of taskObjects) {
    let points = Number(element.estimatedPoints);
    if (element.status === "ToDo") {
      toDo += points;
    } else if (element.status === "In Progress") {
      inProgess += points;
    } else if (element.status === "Code Review") {
      codeReview += points;
    } else if (element.status === "Done") {
      donePoints += points;
    }
  }



  console.log(`ToDo: ${toDo}pts`)
  console.log(`In Progress: ${inProgess}pts`)
  console.log(`Code Review: ${codeReview}pts`)
  console.log(`Done Points: ${donePoints}pts`)

  if (donePoints >= inProgess + toDo + codeReview){
    console.log(`Sprint was successful!`)
  } else {
    console.log(`Sprint was unsuccessful...`)
  }

  function removeTask(assignee, index) {
    const matchingTasks = taskObjects.filter((task) => task.assignee === assignee);

    if (matchingTasks.length === 0) {
      console.log(`Assignee ${assignee} does not exist on the board!`);
      return;
    }

    if (index < 0 || index >= matchingTasks.length) {
      console.log("Index is out of range!");
      return;
    }

    const taskIndexToRemove = taskObjects.findIndex(
        (task) => task.assignee === assignee && task.taskId === matchingTasks[index].taskId
    );

    if (taskIndexToRemove === -1) {
      console.log(`Task with index ${index} does not exist for ${assignee}!`);
      return;
    }

    taskObjects.splice(taskIndexToRemove, 1);
  }

  function addNewTask(assignee, taskId, title, status, estimatedPoints) {
    const existingAssignee = taskObjects.find(
      (task) => task.assignee === assignee
    );
    if (existingAssignee) {
      const newTask = {
        assignee,
        taskId,
        title,
        status,
        estimatedPoints,
      };
      taskObjects.push(newTask);
    } else {
      console.log(`Assignee ${assignee} does not exist on the board!`);
    }
  }

  function changeTaskStatus(assignee, taskId, newStatus) {
    const existingAssignee = taskObjects.find(
      (task) => task.assignee === assignee
    );

    if (existingAssignee) {
      const taskToUpdate = taskObjects.find((task) => task.taskId === taskId);

      if (taskToUpdate) {
        taskToUpdate.status = newStatus;
      } else {
        console.log(`Task with ID ${taskId} does not exist for ${assignee}!`);
      }
    } else {
      console.log(`Assignee ${assignee} does not exist on the board!`);
    }
  }
}

// solve([
//   "5",
//   "Kiril:BOP-1209:Fix Minor Bug:ToDo:3",
//   "Mariya:BOP-1210:Fix Major Bug:In Progress:3",
//   "Peter:BOP-1211:POC:Code Review:5",
//   "Georgi:BOP-1212:Investigation Task:Done:2",
//   "Mariya:BOP-1213:New Account Page:In Progress:13",
//   "Add New:Kiril:BOP-1217:Add Info Page:In Progress:5",
//   "Change Status:Peter:BOP-1290:ToDo",
//   "Remove Task:Mariya:1",
//   "Remove Task:Joro:1",
// ]);

solve(  [
  '4',
  'Kiril:BOP-1213:Fix Typo:Done:1',
  'Peter:BOP-1214:New Products Page:In Progress:2',
  'Mariya:BOP-1215:Setup Routing:ToDo:8',
  'Georgi:BOP-1216:Add Business Card:Code Review:3',
  'Add New:Sam:BOP-1237:Testing Home Page:Done:3',
  'Change Status:Georgi:BOP-1216:Done',
  'Change Status:Will:BOP-1212:In Progress',
  'Remove Task:Georgi:3',
  'Change Status:Mariya:BOP-1215:Done',
])
