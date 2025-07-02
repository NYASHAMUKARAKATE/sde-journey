const name = "Nyasha";

// For loop: Counting up
for (let i = 1; i <= 5; i++) {
  console.log(`${name}'s counter: ${i}`);
}

// While loop: Simple countdown
let count = 3;
while (count > 0) {
  console.log(`${name} is counting down: ${count}`);
  count--;
}

// Do-while: Practice reps
let reps = 1;
do {
  console.log(`${name} completed rep ${reps}`);
  reps++;
} while (reps <= 3);

// For...of: Favorite fruits
const fruits = ["Apple", "Banana", "Cherry"];
for (const fruit of fruits) {
  console.log(`${name} likes ${fruit}`);
}

// For...in: Profile properties
const profile = { username: "nyasha", level: "beginner", active: true };
for (const key in profile) {
  console.log(`${name}'s ${key}: ${profile[key]}`);
}