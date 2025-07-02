// Primitive Types
const str = "Hello, I am Nyasha";
const num = 42;
const bool = true;
const nothing = null;
let notDefined;
const sym = Symbol('unique');
const bigInt = 9007199254740991n;

// Reference Types
const obj = { 
  name: "Nyasha", 
  age: 21,
  isAdmin: false
};
const arr = [1, "two", false, { key: "value" }];
function greet() { return "Hello!"; }

console.log(typeof str);
console.log(typeof num);
console.log(typeof bool);
console.log(typeof nothing);
console.log(typeof notDefined);
console.log(typeof sym);
console.log(typeof bigInt);

console.log(typeof obj);
console.log(typeof arr);