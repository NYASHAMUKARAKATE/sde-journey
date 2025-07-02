// Function declaration (hoisted)
function greet(name) {
  return `Hello, ${name}! Welcome to your coding journey.`;
}

// Function expression
const add = function(a, b) {
  return `${a} + ${b} = ${a + b}`;
};

// Default parameters
function createUser(name, role = "user", active = true) {
  return { 
    name, 
    role, 
    active,
    welcome: `Hi ${name}, your role is ${role}.`
  };
}

// Arrow function:
const farewell = name => `Goodbye, ${name}! See you soon.`;


console.log(greet("Nyasha")); 
console.log(add(2, 3));      
console.log(createUser("Mukarakate", "admin"));