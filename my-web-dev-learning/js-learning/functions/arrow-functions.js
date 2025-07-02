const name = "Nyasha";

// Arrow function: square a number
const square = n => n * n;

// Arrow function: multiply two numbers
const multiply = (a, b) => a * b;

// Arrow function: create a person object
const createPerson = (personName, age) => ({
  name: personName,
  age,
  isAdult: age >= 18,
  greeting: `Hello, I'm ${personName} and I'm ${age} years old.`
});

// Arrow function: create an item object
const createItem = (id, itemName) => ({
  id,
  name: itemName,
  owner: name
});

console.log(square(4)); // 16
console.log(multiply(3, 4)); // 12
console.log(createPerson("Nyasha", 21));
console.log(createItem(1, "Book"));