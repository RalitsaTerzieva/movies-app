from django.shortcuts import render
from rest_framework import viewsets
from .models import Moviedata
from .serializers import MovieSerializer

# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer
    
class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(type_movie='action')
    serializer_class = MovieSerializer

class AnimationViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(type_movie='animation')
    serializer_class = MovieSerializer