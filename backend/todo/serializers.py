""" This is needed to convert model instances to JSON so that 
front-end can work with the received data from the back-end database."""

from rest_framework import serializers
from .models import Todo 

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo 
        fields = ('id', 'title', 'description', 'completed')
