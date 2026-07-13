from django.shortcuts import render
from .models import Paste
from .serializers import PasteSerializer
from rest_framework import viewsets
# Create your views here.
from django.db.models import Q
from django.http import Http404
from django.utils import timezone

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate

from .permissions import IsOwnerOrPublicReadOnly

@api_view(['POST'])
def login_api(request):
    try:

        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username = username, password = password)
        if user:
            token = Token.objects.get_or_create(user = user)
            return Response({'status' : 200, 'token' : str(token)})

        return Response({'status' : 300, 'message' : "Invalid Credentials"})

    except Exception as e:
        print(e)
    return Response({
        'status' : 400,
        'message': "Something went wrong"
    })

class PasteModelViewSet(viewsets.ModelViewSet):
    serializer_class = PasteSerializer
    lookup_field = 'slug'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrPublicReadOnly, IsAuthenticated]

    def get_queryset(self):
        return Paste.objects.filter(Q(expires_at__isnull=True) | Q(expires_at__gt=timezone.now())).filter(Q(is_private = False) | Q(user = self.request.user))
    
    
    def get_object(self):
        obj = super().get_object()
        if obj.is_expired:
            raise Http404
        return obj


    def perform_create(self, serializer):
        serializer.save(user = self.request.user)



