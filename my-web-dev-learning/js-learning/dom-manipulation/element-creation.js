const newDiv = document.createElement('div');
const newParagraph = document.createElement('p');
const newButton = document.createElement('button');

newDiv.id = "new-div";
newDiv.className = "box";
newParagraph.textContent = "This is a dynamically created paragraph for Nyasha!";
newButton.textContent = "Click Me, Nyasha!";
newButton.className = "btn";

newButton.addEventListener('click', () => {
  newParagraph.textContent = "You clicked the button, Nyasha!";
  newDiv.style.backgroundColor = "#b8c1ec";
});

newDiv.appendChild(newParagraph);
newDiv.appendChild(newButton);
document.body.appendChild(newDiv);

if (header) {
  header.style.backgroundColor = "#333";
  header.style.color = "#fff";
  header.classList.add('dark-header');
  header.classList.remove('old-class');
  header.classList.toggle('fixed-header');
}

// Add a new list dynamically
const fruitList = document.createElement('ul');
fruitList.id = "nyasha-fruits";
["Apple", "Banana", "Cherry"].forEach(fruit => {
  const li = document.createElement('li');
  li.textContent = `${fruit} (Nyasha's favorite)`;
  fruitList.appendChild(li);
});
document.body.appendChild(fruitList);