from rest_framework.views import APIView
from ElectionManager.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from collections import defaultdict


class ElectionView(APIView):

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
                    return Response({}, status=status.HTTP_400_BAD_REQUEST)
            return Response({}, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        try:
            id = request.query_params.get('id')
            if id:
                try:
                    elections = Election.objects.all().filter(id=id)
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

    def delete(self, request, format=None):
        id = request.data.get('id')
        try:
            instance = Election.objects.get(id=id)
        except Election.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        try:
            instance.delete()
            return Response({}, status=status.HTTP_200_OK)
        except:
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, format=None):
        try:
            instance = Election.objects.get(id=request.data.get('id'))
            if request.data.get('Title'):
                instance.Title = request.data.get('Title')
            if request.data.get('Start_Time'):
                instance.Title = request.data.get('Start_Time')
            if request.data.get('End_Time'):
                instance.Title = request.data.get('End_Time')
            if request.data.get('Number_Of_Votes'):
                instance.Title = request.data.get('Number_Of_Votes')
            instance.save()
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        if request.data.get('ListOfChoices'):
            list_of_choices = request.data.get('ListOfChoices')
            id = request.data.get('id')
            old_list_of_choices = ListOfChoices.objects.all().filter(Election_ref=id)
            for old_choice in old_list_of_choices:
                old_choice.delete()
            for choice in list_of_choices:
                choice_data = {
                    'Title': choice,
                    'Election_ref': id
                }
                list_of_choices_serializer = ListOfChoicesSerializer(data= choice_data)
                if list_of_choices_serializer.is_valid():
                    list_of_choices_serializer.save()
                else:
                    return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_200_OK)


class VoteView(APIView):

    def put(self, request, format=None):
        try:
            election_instance = Election.objects.get(id=request.data.get('id'))
            election_instance.Number_Of_Votes = election_instance.Number_Of_Votes + 1
            election_instance.save()
            return Response({}, status=status.HTTP_200_OK)
        except:
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ChoicesView(APIView):

    def get(self, request, format=None):
        choices = ListOfChoices.objects.all().filter(Election_ref=request.query_params.get('id'))
        out = []
        for choice in choices:
            out.append(choice.Title)
        return Response(out, status=status.HTTP_200_OK)

