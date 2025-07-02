document.addEventListener('DOMContentLoaded', () => {
  // Try to get the user's name from localStorage
  let userName = localStorage.getItem('userName');
  // If there's no name saved, ask the user for their name
  if (!userName) {
    userName = prompt("Welcome! What's your name?");
    // If the user doesn't enter anything, use "Friend" as a default
    if (!userName || !userName.trim()) userName = "Friend";
    // Save the name for next time
    localStorage.setItem('userName', userName);
  }

  // Get references to all the important elements on the page
  const form = document.getElementById('task-form');
  const taskInput = document.getElementById('task-input');
  const categorySelect = document.getElementById('category');
  const dueDateInput = document.getElementById('due-date');
  const taskList = document.getElementById('task-list');
  const filter = document.getElementById('filter');
  const markAllBtn = document.getElementById('mark-all');
  const clearAllBtn = document.getElementById('clear-all');
  const counter = document.getElementById('counter');
  const greeting = document.getElementById('greeting');

  // Change the input placeholder to include the user's name
  taskInput.placeholder = `What's on your mind, ${userName}?`;

  // Show a greeting based on the time of day
  function setGreeting() {
    const hour = new Date().getHours();
    let msg = `Hello, ${userName}!`;
    if (hour < 12) msg = `Good morning, ${userName}! ☀️`;
    else if (hour < 18) msg = `Good afternoon, ${userName}! 🌤️`;
    else msg = `Good evening, ${userName}! 🌙`;
    greeting.textContent = msg;
  }
  setGreeting();

  // Try to get tasks from localStorage, or start with an empty list
  let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

  // Show all the tasks when the page loads
  renderAllTasks();

  // When the form is submitted, add a new task
  form.addEventListener('submit', (e) => {
    e.preventDefault(); // Stop the page from reloading
    const text = taskInput.value.trim();
    const category = categorySelect.value;
    const dueDate = dueDateInput.value;

    // Only add the task if all fields are filled in
    if (text && category && dueDate) {
      const task = {
        id: Date.now(), // Unique id for the task
        text,
        category,
        dueDate,
        completed: false,
      };
      tasks.push(task); // Add the new task to the list
      saveTasks(); // Save the tasks to localStorage
      renderTask(task, true); // Show the new task with animation
      form.reset(); // Clear the form
      updateCounter(); // Update the task counter
    }
  });

  // When the filter changes, show the right tasks
  filter.addEventListener('change', renderAllTasks);

  // When "Mark All as Done" is clicked, mark every task as completed
  markAllBtn.addEventListener('click', () => {
    tasks.forEach(t => t.completed = true);
    saveTasks();
    renderAllTasks();
  });

  // When "Clear All" is clicked, remove all tasks after confirming
  clearAllBtn.addEventListener('click', () => {
    if (confirm(`Are you sure you want to clear all tasks, ${userName}?`)) {
      // Add animation to each task before removing
      Array.from(taskList.children).forEach(li => {
        li.classList.add('removing');
      });
      setTimeout(() => {
        tasks = [];
        saveTasks();
        renderAllTasks();
      }, 300);
    }
  });

  // Show all tasks, using the current filter
  function renderAllTasks() {
    taskList.innerHTML = '';
    let filtered = [...tasks];
    if (filter.value === 'completed') {
      filtered = filtered.filter(t => t.completed);
    } else if (filter.value === 'pending') {
      filtered = filtered.filter(t => !t.completed);
    }
    filtered.forEach(task => renderTask(task));
    updateCounter();
  }

  // Show one task on the page (with optional animation)
  function renderTask(task, animate = false) {
    const li = document.createElement('li');
    li.className = task.completed ? 'completed' : '';
    if (animate) li.classList.add('adding');
    li.innerHTML = `
      <div>
        <strong>${task.text}</strong>
        <small>${task.category} | Due: ${task.dueDate}</small>
      </div>
      <div>
        <button class="toggle-btn">${task.completed ? 'Undo' : 'Done'}</button>
        <button class="delete-btn">Delete</button>
      </div>
    `;

    // When the "Done"/"Undo" button is clicked, toggle the task's completed state
    li.querySelector('.toggle-btn').onclick = () => {
      task.completed = !task.completed;
      saveTasks();
      renderAllTasks();
    };

    // When the "Delete" button is clicked, remove the task with animation
    li.querySelector('.delete-btn').onclick = () => {
      li.classList.add('removing');
      setTimeout(() => {
        tasks = tasks.filter(t => t.id !== task.id);
        saveTasks();
        renderAllTasks();
      }, 300);
    };

    taskList.appendChild(li);

    // Remove the animation class after the animation is done
    if (animate) {
      setTimeout(() => li.classList.remove('adding'), 400);
    }
  }

  // Save the tasks to localStorage
  function saveTasks() {
    localStorage.setItem('tasks', JSON.stringify(tasks));
  }

  // Update the counter that shows how many tasks there are
  function updateCounter() {
    const total = tasks.length;
    const completed = tasks.filter(t => t.completed).length;
    const pending = total - completed;
    counter.textContent = `Total: ${total} | Completed: ${completed} | Pending: ${pending}`;
  }
});
