import random
import string

def generate_secret_key():
    # Supprimer les caractères spéciaux qui pourraient poser problème dans les shells
    chars_to_exclude = "\"\\'`&{}[]$!()^:<>"
    valid_chars = string.ascii_letters + string.digits + string.punctuation
    valid_chars = ''.join(c for c in valid_chars if c not in chars_to_exclude)

    secret_key = ''.join(random.choice(valid_chars) for i in range(50))
    return secret_key

# Générer la clé et ajouter le préfixe "django-insecure-"
generated_key = generate_secret_key()
complete_secret_key = "django-insecure-" + generated_key

print(complete_secret_key)
