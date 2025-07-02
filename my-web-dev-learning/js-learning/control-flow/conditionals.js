const temperature = 25;
const name = "Nyasha";

// If-else
if (temperature > 30) {
  console.log(`It's hot outside, ${name}. Stay hydrated!`);
} else if (temperature > 20) {
  console.log(`It's warm outside, ${name}. A perfect day for a walk!`);
} else {
  console.log(`It's cool outside, ${name}. Maybe grab a jacket!`);
}

// Switch-case
const day = "Wednesday";
let dayType;

switch(day) {
  case "Monday":
  case "Tuesday":
  case "Wednesday":
  case "Thursday":
  case "Friday":
    dayType = "Weekday";
    break;
  case "Saturday":
  case "Sunday":
    dayType = "Weekend";
    break;
  default:
    dayType = "Invalid day";
}

if (dayType === "Weekday") {
  console.log(`${day} is a ${dayType}. Time to be productive, ${name}!`);
} else if (dayType === "Weekend") {
  console.log(`${day} is a ${dayType}. Enjoy your rest, ${name}!`);
} else {
  console.log(`"${day}" is not a valid day, ${name}. Please check your calendar.`);
}