from .models import *
from rest_framework import serializers

class ListOfChoicesSerializer(serializers.ModelSerializer):
    Election = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = ListOfChoices

class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election