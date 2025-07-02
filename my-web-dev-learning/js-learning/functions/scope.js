const name = "Nyasha";

// Global scope
const globalVar = `I'm global and visible everywhere, ${name}.`;

function scopeDemo() {
  // Function scope
  const functionVar = `I'm in function scope, only visible inside scopeDemo, ${name}.`;
  
  if (true) {
    // Block scope
    let blockVar = `I'm in block scope, only visible in this block, ${name}.`;
    console.log(globalVar);
    console.log(functionVar);   
    console.log(blockVar);       
  }
  
  // Uncommenting the next line would cause an error:
  // console.log(blockVar); // ReferenceError: blockVar is not defined
}

scopeDemo();

// Hoisting example
console.log(hoistedVar); // undefined (var is hoisted but not initialized)
var hoistedVar = `This variable is hoisted, ${name}.`;

// Uncommenting the next line would cause an error:
// console.log(letVar); // ReferenceError (let is not hoisted)
let letVar = `This variable is block-scoped, ${name}.`;