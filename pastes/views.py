from django.shortcuts import render
from .models import Paste
from .serializers import PasteSerializer
from rest_framework import viewsets
# Create your views here.

class PasteModelViewSet(viewsets.ModelViewSet):
    serializer_class = PasteSerializer
    queryset = Paste.objects.all()
    lookup_field = 'slug'
    

