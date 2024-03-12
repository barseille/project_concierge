// Menu Hamburger
document.addEventListener("DOMContentLoaded", () => {
    const toggleMenuBtn = document.querySelector("#menu-btn");
    const toggledMenu = document.querySelector("#toggled-menu");
    const menuIcon = document.querySelector("#menu-btn .material-symbols-outlined:first-child");
    const closeIcon = document.querySelector("#menu-btn .material-symbols-outlined:last-child");
  
    toggleMenuBtn.addEventListener("click", () => {
      toggledMenu.classList.toggle("hidden");
      menuIcon.classList.toggle("hidden");
      closeIcon.classList.toggle("hidden");
      const isExpanded = toggleMenuBtn.getAttribute("aria-expanded") === "true";
      toggleMenuBtn.setAttribute("aria-expanded", !isExpanded);
    });
  });

// Ici, on écoute le chargement du DOM. Ensuite, on sélectionne le bouton du menu et le menu lui-même. On ajoute un écouteur d'événement sur le bouton qui bascule la classe hidden pour montrer et cacher le menu et changer l'icône.