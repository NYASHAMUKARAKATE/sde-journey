// Array creation
const fruits = ["Apple", "Banana"];

// Basic operations
fruits.push("Orange");     // Add to end
fruits.unshift("Mango");   // Add to beginning
fruits.pop();              // Remove from end
fruits.shift();            // Remove from beginning

console.log(fruits); // Current fruits array

// Modern array methods
const numbers = [1, 2, 3, 4, 5];

// Map: transform each element
const doubled = numbers.map(num => num * 2);

// Filter: select elements
const evens = numbers.filter(num => num % 2 === 0);

// Reduce: accumulate values
const sum = numbers.reduce((total, num) => total + num, 0);

// Find: first matching element
const firstEven = numbers.find(num => num % 2 === 0);

// Some: test if any match
const hasEven = numbers.some(num => num % 2 === 0);

// Every: test if all match
const allEven = numbers.every(num => num % 2 === 0);

console.log("Doubled:", doubled);
console.log("Even numbers:", evens);
console.log("Sum:", sum);
console.log("First even:", firstEven);
console.log("Has even?", hasEven);
console.log("All even?", allEven);

const name = "Nyasha";
const favNumbers = numbers.filter(num => num > 2);
console.log(`${name}'s favorite numbers above 2:`, favNumbers);

// Loop through fruits with index
fruits.push("Pineapple", "Grapes");
for (let i = 0; i < fruits.length; i++) {
  console.log(`${name} likes fruit #${i + 1}: ${fruits[i]}`);
}