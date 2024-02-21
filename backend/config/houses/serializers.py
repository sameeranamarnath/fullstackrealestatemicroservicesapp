from rest_framework import serializers

from .models import House 

class HouseSerializer(serializers.ModelSerializer):
  model= 'House'
  fields= '__all__'     #[ 'id', 'name']

