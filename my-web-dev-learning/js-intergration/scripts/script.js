const messages = [
    "Button clicked! JavaScript is powerful.",
    "Keep going, Nyasha! Every click is progress.",
    "Tip: Practice a little every day.",
    "Debugging is just problem-solving in disguise.",
    "You’re building your skills, one step at a time!",
    "Remember: Even experts were beginners once."
];

document.getElementById('myButton').addEventListener('click', function() {
    const output = document.getElementById('output');
    const randomIndex = Math.floor(Math.random() * messages.length);
    output.textContent = messages[randomIndex];
    output.style.color = '#4caf50';
});

document.getElementById('clearBtn').addEventListener('click', function() {
    const output = document.getElementById('output');
    output.textContent = '';
});