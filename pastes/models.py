from django.db import models
from django.contrib.auth.models import User
from .utils import generate_unique_slug
# Create your models here.

class Paste(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paste', null = True, blank = True)
    content = models.CharField(max_length = 100)
    slug = models.CharField(max_length=10, unique = True, db_index = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug()
        super().save(*args, **kwargs)