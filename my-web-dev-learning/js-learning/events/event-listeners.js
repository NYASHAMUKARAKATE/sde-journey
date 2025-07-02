document.addEventListener('DOMContentLoaded', () => {
  const clickButton = document.getElementById('clickBtn');
  const hoverArea = document.getElementById('hoverArea');
  const textInput = document.getElementById('textInput');

  // Click event
  clickButton.addEventListener('click', (e) => {
    console.log('Button clicked');
    e.target.textContent = 'Clicked!';
  });

  // Mouse events
  hoverArea.addEventListener('mouseenter', () => {
    hoverArea.style.backgroundColor = '#eee';
  });
  
  hoverArea.addEventListener('mouseleave', () => {
    hoverArea.style.backgroundColor = '';
  });

  // Keyboard events
  textInput.addEventListener('keyup', (e) => {
    console.log(`Typed: ${e.target.value}`);
  });

  // Form submission
  const form = document.querySelector('form');
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    console.log('Form submitted');
  });

  // Event delegation
  document.body.addEventListener('click', (e) => {
    if (e.target.classList.contains('item')) {
      console.log(`Item clicked: ${e.target.textContent}`);
    }
  });
});