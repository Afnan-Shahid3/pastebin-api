from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Paste(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paste', null = True, blank = True)
    content = models.CharField(max_length = 100)
    slug = models.CharField(max_length=10, unique = True, db_index = True)
    created_at = models.DateTimeField(auto_now_add = True)

