
document.addEventListener("DOMContentLoaded", function () {
  // Obtient la langue actuelle de Django et définit cette langue comme l'option sélectionnée dans le sélecteur
  var selectedLanguage = "{{ request.LANGUAGE_CODE }}";
  var languageSelector = document.getElementById("languageSelector");
  if (languageSelector) {
    languageSelector.value = selectedLanguage;
  }
});



// // Chargement des traductions depuis un fichier JSON et mise à jour du contenu de la page
// async function loadTranslations() {
//     try {
//       const response = await fetch("translate.json"); // Chemin vers votre fichier de traductions
//       const translations = await response.json(); // Convertit la réponse en JSON
//       return translations; // Retourne les traductions
//     } catch (error) {
//       console.error("Error loading translation file:", error); // Gestion des erreurs
//       return {}; // Retourne un objet vide en cas d'erreur
//     }
//   }

//   // Mise à jour des éléments de la page selon la langue sélectionnée
//   function updatePageContent(lang, translations) {
//       document.querySelectorAll("[data-translate]").forEach((element) => {
//         const key = element.getAttribute("data-translate");
//         if (translations[lang] && translations[lang][key]) {
//           element.textContent = translations[lang][key];
//         }
//       });

//       // Vérifiez l'existence de chaque élément avant de tenter de mettre à jour ses propriétés
//       const placeholders = {
//         "firstName": "firstNamePlaceholder",
//         "lastName": "lastNamePlaceholder",
//         "email": "emailPlaceholder",
//         "phone": "phonePlaceholder",
//         "message": "messagePlaceholder",
//       };

//       Object.entries(placeholders).forEach(([name, placeholderKey]) => {
//         const input = document.getElementsByName(name)[0];
//         if (input && translations[lang] && translations[lang][placeholderKey]) {
//           input.placeholder = translations[lang][placeholderKey];
//         }
//       });

//       const submitButton = document.querySelector("form button[type='submit']");
//       if (submitButton && translations[lang] && translations[lang]["submitButton"]) {
//         submitButton.textContent = translations[lang]["submitButton"];
//       }
//     }

//   document.addEventListener("DOMContentLoaded", async () => {
//     // Charge les traductions et met à jour le contenu selon la langue stockée ou par défaut
//     const translations = await loadTranslations();
//     const languageSelector = document.getElementById("languageSelector");
//     const storedLanguage = localStorage.getItem("language") || "en"; // Langue par défaut
//     updatePageContent(storedLanguage, translations); // Mise à jour initiale du contenu

//     // Écoute les changements de langue et met à jour le contenu en conséquence
//     languageSelector.addEventListener("change", function () {
//       const selectedLanguage = this.value;
//       updatePageContent(selectedLanguage, translations);
//       localStorage.setItem("language", selectedLanguage); // Stocke la langue sélectionnée
//     });
//   });
