from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register('pastes', views.PasteModelViewSet, basename='pastes')

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', views.login_api),
    path('api/pastes/<slug:slug>/raw/', views.raw_paste_view, name = 'raw-paste')
]