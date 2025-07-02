
// Creating a promise
const fetchNyasha = new Promise((resolve, reject) => {
  setTimeout(() => {
    const success = Math.random() > 0.2;
    if (success) {
      resolve({ id: 7, name: "Nyasha", role: "Developer" });
    } else {
      reject("Sorry Nyasha, failed to fetch your data.");
    }
  }, 1200);
});

// Using the promise
fetchNyasha
  .then(user => {
    console.log(`Welcome, ${user.name}! Your role is: ${user.role}`);
    return user.id;
  })
  .then(userId => {
    console.log(`Nyasha's user ID: ${userId}`);
  })
  .catch(error => {
    console.error("Error:", error);
  })
  .finally(() => {
    console.log("Nyasha's operation completed");
  });

// Promise.all example with Nyasha's data
const promise4 = Promise.resolve("Hello Nyasha!");
const promise5 = new Promise(resolve => setTimeout(resolve, 200, "Learning JS is fun!"));
const promise6 = fetch('https://jsonplaceholder.typicode.com/users/7').then(res => res.json());

Promise.all([promise4, promise5, promise6])
  .then(values => {
    console.log("All Nyasha's promises resolved:", values);
  })
  .catch(error => {
    console.error("One of Nyasha's promises rejected:", error);
  });