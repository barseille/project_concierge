from django.utils import translation

class AdminLocaleMiddleware:
    '''
    Ce middleware vérifie si la requête concerne l'interface d'administration (en vérifiant si le chemin de la requête commence par /admin/) et force la langue à fr (français) pour ces requêtes.
    '''
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            with translation.override('fr'):
                response = self.get_response(request)
        else:
            response = self.get_response(request)
        return response



