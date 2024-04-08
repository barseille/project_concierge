from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    """ 
    WebsiteUser simule un utilisateur qui visite la page d'accueil et la page de contact. @task décore une méthode pour indiquer qu'il s'agit d'une tâche que l'utilisateur exécutera, et wait_time détermine le temps d'attente entre chaque tâche.
    """
    wait_time = between(1, 5)  # Attente entre chaque tâche (1 à 5 secondes).

    @task()
    def view_contact_page(self):
        self.client.get("/contact/")
