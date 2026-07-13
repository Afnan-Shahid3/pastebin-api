from django.db import models
from django.contrib.auth.models import User
from .utils import generate_unique_slug
from django.utils import timezone
# Create your models here.


class Paste(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paste', null = True, blank = True)
    content = models.CharField(max_length = 100)
    slug = models.CharField(max_length=10, unique = True, db_index = True)
    created_at = models.DateTimeField(auto_now_add = True)
    expires_at = models.DateTimeField(null=True, blank=True)
    is_private = models.BooleanField(default = False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug()
        super().save(*args, **kwargs)

    @property
    def is_expired(self):
        if self.expires_at and self.expires_at < timezone.now():
            return True
        return False