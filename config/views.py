from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Car, Book
from .serializers import CarSerializer, BookSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
