//fetchUser promise
const fetchUser = new Promise((resolve, reject) => {
  setTimeout(() => {
    const success = Math.random() > 0.2;
    if (success) {
      resolve({ id: 21, name: "Nyasha Mukarakate", role: "Developer" });
    } else {
      reject("Sorry Nyasha, could not fetch your user data.");
    }
  }, 1200);
});

// Async function
async function getUserData() {
  try {
    console.log("Fetching Nyasha's user data...");
    const user = await fetchUser;
    console.log("User received:", user);

    // Simulate another async operation
    const userPosts = await new Promise(resolve => {
      setTimeout(() => {
        resolve([
          { id: 1, title: "Nyasha's First Post" },
          { id: 2, title: "Learning Async JS" }
        ]);
      }, 1000);
    });

    console.log("Nyasha's posts:", userPosts);
    return { user, posts: userPosts };
  } catch (error) {
    console.error("Error in getUserData:", error);
    throw error;
  }
}

// Calling async function
getUserData()
  .then(data => console.log("Final data for Nyasha:", data))
  .catch(error => console.error("Final error for Nyasha:", error));

// Async IIFE
(async () => {
  try {
    const data = await getUserData();
    console.log("IIFE result for Nyasha:", data);
  } catch (error) {
    console.error("IIFE error for Nyasha:", error);
  }
})();