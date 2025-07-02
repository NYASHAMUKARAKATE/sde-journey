document.addEventListener("DOMContentLoaded", () => {
  const typingEl = document.querySelector(".typing");
  const text = "Nyasha Mukarakate";
  let index = 0;
  function type() {
    if (index < text.length) {
      typingEl.innerHTML += text.charAt(index);
      index++;
      setTimeout(type, 100);
    }
  }
  type();

  const addProjectBtn = document.getElementById("addProjectBtn");
  const projectGrid = document.getElementById("projectGrid");

  addProjectBtn.addEventListener("click", () => {
    
    const title = prompt("Enter the project title:");
    if (!title) return;
    const description = prompt("Describe your project:");
    if (!description) return;
    const imgUrl = prompt("Enter image URL (leave blank for default):") || "assets/placeholder.png";

    const newCard = document.createElement("div");
    newCard.classList.add("project-card");
    newCard.innerHTML = `
      <img src="${imgUrl}" alt="${title} Screenshot" />
      <h3>${title}</h3>
      <p>${description}</p>
    `;
    projectGrid.appendChild(newCard);
  });
});
