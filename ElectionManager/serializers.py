from .models import *
from rest_framework import serializers

class ListOfChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfChoices
        fields = ('Title', 'Election_ref')

class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = ('id', 'Title', 'Start_Time', 'End_Time', 'Number_Of_Votes')