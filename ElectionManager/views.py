from rest_framework.views import APIView
from ElectionManager.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from collections import defaultdict


class ElectionView(APIView):
    """
     get path between two nodes
    """

    def post(self, request, format=None):
        election_data = request.data
        election_serializer = ElectionSerializer(data=election_data)
        if election_serializer.is_valid(raise_exception=True):
            election_data_saved = election_serializer.save()
        list_of_choices = request.data.get('ListOfChoices')
        list_of_choices_serializer = []
        for i in list_of_choices:
            list_of_choices[i].election
            list_of_choices_serializer[i] = ListOfChoicesSerializer(data=list_of_choices[i])
            if list_of_choices_serializer[i].is_valid(raise_exception=True):
                list_of_choices_saved = list_of_choices_serializer[i].save()

        return Response({}, status=status.HTTP_200_OK)