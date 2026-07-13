from .models import Paste
from rest_framework import serializers

class PasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paste
        fields = ['id', 'user', 'content','slug', 'created_at', 'expires_at', 'is_private']
        read_only_fields = ['created_at', 'slug']



