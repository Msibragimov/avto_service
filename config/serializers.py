from rest_framework import serializers

from config.models import Car, Book


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'name', 'author', 'published']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        models = Book
        fields = ['user', 'avto', 'booked_from', 'booked_to']