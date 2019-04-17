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
            for choice in list_of_choices:
                list_of_choices_data = {
                    'Title': choice,
                    'Election_ref': election_data_saved.id
                }
                list_of_choices_serializer = ListOfChoicesSerializer(data=list_of_choices_data)
                if list_of_choices_serializer.is_valid(raise_exception=True):
                    list_of_choices_saved = list_of_choices_serializer.save()
                else:
                    return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response({}, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, format=None):
        try:
            id = request.query_params.get('id')
            if id:
                try:
                    elections = Election.objects.get(id=id)
                except Election.DoesNotExist:
                    return Response({}, status=status.HTTP_404_NOT_FOUND)
                data = {}
                for e in elections:
                    data = {
                        'id': e.id,
                        'Title': e.Title,
                        'Start_Time': e.Start_Time,
                        'End_Time': e.End_Time,
                        'Number_Of_Votes': e.Number_Of_Votes
                    }
                return Response(data, status=status.HTTP_200_OK)
            else:
                elections = Election.objects.all()
                data = []
                for e in elections:
                    data.append({
                        'id': e.id,
                        'Title': e.Title
                    })
                return Response(data, status=status.HTTP_200_OK)
        except:
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
