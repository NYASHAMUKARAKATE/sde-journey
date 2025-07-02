// Callback functions
function fetchNyashaData(callback) {
  setTimeout(() => {
    const data = { id: 21, name: "Nyasha Mukarakate", role: "Developer" };
    callback(null, data); // First param for error, second for data
  }, 1200);
}

function processNyashaData(error, data) {
  if (error) {
    console.error("Error:", error);
    return;
  }
  console.log(`Data received for ${data.name}:`, data);
}

// Using the callback
fetchNyashaData(processNyashaData);

// Callback hell example, Nyasha style
function step1(callback) {
  setTimeout(() => {
    console.log("Nyasha finished Step 1");
    callback();
  }, 1000);
}

function step2(callback) {
  setTimeout(() => {
    console.log("Nyasha finished Step 2");
    callback();
  }, 1500);
}

function step3(callback) {
  setTimeout(() => {
    console.log("Nyasha finished Step 3");
    callback();
  }, 500);
}

// Pyramid of doom
step1(() => {
  step2(() => {
    step3(() => {
      console.log("Nyasha completed all steps!");
    });
  });
});