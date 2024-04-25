import random
import string

def generate_secret_key():
    # Supprimer les caractères spéciaux "\" pour éviter les problèmes
    characters = string.ascii_letters + string.digits + string.punctuation.replace("\\", "").replace("'", "").replace('"', '')
    secret_key = ''.join(random.choice(characters) for i in range(50))
    return secret_key

# Générer la clé et ajouter le préfixe django-insecure
generated_key = generate_secret_key()
complete_secret_key = "django-insecure-" + generated_key

print(complete_secret_key)
