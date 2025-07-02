// Object creation
const person = {
  firstName: "Nyasha",
  lastName: "Mukarakate",
  age: 21,
  hobbies: ["coding", "reading", "football"],
  address: {
    street: "292 Langa Street",
    city: "Meyerton"
  },
  // Method to get full name
  getFullName: function() {
    return `${this.firstName} ${this.lastName}`;
  },
  // Shorthand method (ES6)
  greet() {
    return `Hello, I'm ${this.getFullName()} from ${this.address.city}!`;
  }
};

// Accessing properties
console.log(person.firstName);  
console.log(person["lastName"]);       
console.log(person.getFullName());     
console.log(person.greet());           

// Modifying objects
person.age = 22;
person.job = "Software Developer";
person.hobbies.push("gaming");

// Object methods
const keys = Object.keys(person);
const values = Object.values(person);
const entries = Object.entries(person);

console.log(keys);    
console.log(values);  
console.log(entries);

// Loop through hobbies
for (const hobby of person.hobbies) {
  console.log(`${person.firstName} enjoys ${hobby}`);
}