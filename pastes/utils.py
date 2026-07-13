import random

# Create your tests here.

def generate_unique_slug():
    from .models import Paste
    base62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    

    while True:
        code = []
        for i in range(6):
            random_word = random.choice(base62)
            code.append(random_word)

        word = "".join(code)
        if Paste.objects.filter(slug = word).exists() == False:
            return word
