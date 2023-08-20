let objList = [
    { id: 1, name: "John" },
    { id: 2, name: "Jane" },
    { id: 3, name: "Bob" }
];

// Check if string "John" is present in the array of objects
const isPresent = objList.some(obj => obj.name === "Rado");

console.log(isPresent); // true