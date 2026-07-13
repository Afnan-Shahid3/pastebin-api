from django.shortcuts import render
from .models import Paste
from .serializers import PasteSerializer
from rest_framework import viewsets
# Create your views here.
from django.db.models import Q
from django.http import Http404
from django.utils import timezone


class PasteModelViewSet(viewsets.ModelViewSet):
    serializer_class = PasteSerializer
    def get_queryset(self):
        return Paste.objects.filter(Q(expires_at__isnull=True) | Q(expires_at__gt=timezone.now()))
    lookup_field = 'slug'
    
    def get_object(self):
        obj = super().get_object()
        if obj.is_expired:
            raise Http404
        return obj

