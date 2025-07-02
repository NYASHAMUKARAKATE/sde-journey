// Array destructuring
const colors = ["red", "green", "blue"];
const [firstColor, secondColor, thirdColor] = colors;

console.log(firstColor);
console.log(secondColor);

// Skipping items
const [primary, , tertiary] = colors;
console.log(primary);
console.log(tertiary);

// Object destructuring
const user = {
  id: 1,
  name: "Nyasha",
  email: "nyasha@gmail.com",
  address: {
    city: "Harare",
    zip: "00263"
  }
};

const { name, email, address: { city } } = user;

console.log(name);
console.log(email);
console.log(city);

// Function parameter destructuring
function printUser({ name, email }) {
  console.log(`Name: ${name}, Email: ${email}`);
}

printUser(user);

// New code additions
const numbers = [10, 20, 30, 40];
const [fav, , , last] = numbers;
console.log(`Nyasha's favorite number: ${fav}, last number: ${last}`);

const settings = {
  theme: "dark",
  language: "en",
  notifications: true
};
function showSettings({ theme, language }) {
  console.log(`Theme: ${theme}, Language: ${language}`);
}