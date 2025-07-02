// DOM Selection Methods

// Get element by ID
const header = document.getElementById('header');

// Get elements by class name
const buttons = document.getElementsByClassName('btn');

// Get elements by tag name
const paragraphs = document.getElementsByTagName('p');

// Query selector (single element)
const mainContainer = document.querySelector('.container');

// Query selector all (multiple elements)
const navItems = document.querySelectorAll('nav li');

console.log("Header element:", header);
console.log("Buttons:", buttons);
console.log("Paragraphs:", paragraphs);
console.log("Main container:", mainContainer);
console.log("Navigation items:", navItems);

// Traversal
const firstChild = mainContainer.firstElementChild;
const lastChild = mainContainer.lastElementChild;
const parent = mainContainer.parentElement;

console.log("First child in container:", firstChild);
console.log("Last child in container:", lastChild);
console.log("Parent of container:", parent);

navItems.forEach(item => {
  item.style.backgroundColor = "#eebbc3";
  item.textContent += " (Nyasha)";
});