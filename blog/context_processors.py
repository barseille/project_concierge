
from .models import Service

def services_processor(request):
    """ 
    Rendre la liste des objets 'Service' disponibles globalement dans tous les templates. Initialement prévu pour les liens de chaques pages de services depuis la page home.
    """
    return {'services': Service.objects.all()}
