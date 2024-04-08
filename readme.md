# Gestion Locative avec ANGKOR MANAGEMENT

## À Propos du Projet

Ce projet Django est une simulation d'un système de gestion locative pour ANGKOR MANAGEMENT, une entreprise fictive de gestion immobilière basée au Cambodge. Il met en évidence les compétences en développement backend à travers la gestion des formulaires, l'interaction avec une base de données, l'envoi d'emails, et l'internationalisation.

## Fonctionnalités Clés

- **Formulaires de Contact et de Soumission :** Implémentation de formulaires pour la soumission de demandes de contact et la gestion des réponses.
- **Gestion de Contenu Dynamique :** Affichage et gestion des services, témoignages, FAQs, et informations sur l'entreprise à partir de la base de données.
- **Internationalisation :** Prise en charge de plusieurs langues pour rendre l'application accessible à un public international.
- **Envoi d'Emails :** Configuration de l'envoi d'emails automatiques en réponse aux soumissions de formulaires.

## Tests

Ce projet inclut des tests unitaires et d'intégration pour s'assurer de la fiabilité et de la qualité du code. Les tests de performance ont également été effectués pour optimiser les temps de réponse de l'application.

Pour exécuter les tests, utilisez la commande :
```
python manage.py test
```

## Technologies Utilisées:

- **Backend :** Django (Python)
- **Base de Données :** Postgres (production sur Heroku)
- **Frontend :** HTML, CSS, TailwindCSS pour le stylisme
- **Déploiement :** Heroku

## Démarrage Rapide

### Cloner le projet depuis votre éditeur de code : 
```
https://github.com/barseille/project_AL.git
```

### Installez les dépendances :
```
pip install -r requirements.txt
```

### Démarrez Tailwind CSS en mode développement (si nécessaire) :
```
python manage.py tailwind start
```

## Exécutez les migrations :
```
python manage.py migrate

```
## Lancez le serveur de développement :
```
python manage.py runserver
```

