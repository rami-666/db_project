from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import views
from .models import (           #add models here
Playoff,
Conference,
Series, 
Division, 
Stadium, 
Team, 
Player,
Game,
)  
from .serializers import (      #add  seiralizers here
PlayoffSerializer, 
ConferenceSerializer, 
SeriesSerializer, 
DivisionSerializer, 
StadiumSerializer, 
TeamSerializer, 
PlayerSerializer,
GameSerializer,
)  


# Create your views here.
class PlayoffApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the monthly sales of the department
        '''
        # print(request.META)

        # if request.META.get("HTTP_YEAR") is None or request.META.get("HTTP_MONTH") is None:
        #     playoffs = Playoff.objects.all()
        # else:
        #     year = request.META.get("HTTP_YEAR")
        #     month = request.META.get("HTTP_MONTH")
        #     domestics = Domestic.objects.filter( date__month__gte=month, date__month__lt=str(int(month)+1), date__year__gte=year, date__year__lt=str(int(year)+1))

        playoffs = Playoff.objects.all()

        serializer = PlayoffSerializer(playoffs, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

        # response["Access-Control-Allow-Origin"] = "*"
        # response["Access-Control-Allow-Methods"] = "GET, POST"
        # response["Access-Control-Max-Age"] = "1000"
        # response["Access-Control-Allow-Headers"] = "year, month, Content-Type"

        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        data = {
            'season': request.data.get('season')
        }
        serializer = PlayoffSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ConferenceApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the monthly sales of the department
        '''
        # print(request.META)

        # if request.META.get("HTTP_YEAR") is None or request.META.get("HTTP_MONTH") is None:
        #     playoffs = Playoff.objects.all()
        # else:
        #     year = request.META.get("HTTP_YEAR")
        #     month = request.META.get("HTTP_MONTH")
        #     domestics = Domestic.objects.filter( date__month__gte=month, date__month__lt=str(int(month)+1), date__year__gte=year, date__year__lt=str(int(year)+1))

        conferences = Conference.objects.all()

        serializer = ConferenceSerializer(conferences, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

        # response["Access-Control-Allow-Origin"] = "*"
        # response["Access-Control-Allow-Methods"] = "GET, POST"
        # response["Access-Control-Max-Age"] = "1000"
        # response["Access-Control-Allow-Headers"] = "year, month, Content-Type"

        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        data = {
            'name': request.data.get('name'),
            'hasPlayoffs': request.data.get('hasPlayoffs')
        }
        serializer = ConferenceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SeriesApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the monthly sales of the department
        '''
        # print(request.META)

        # if request.META.get("HTTP_YEAR") is None or request.META.get("HTTP_MONTH") is None:
        #     playoffs = Playoff.objects.all()
        # else:
        #     year = request.META.get("HTTP_YEAR")
        #     month = request.META.get("HTTP_MONTH")
        #     domestics = Domestic.objects.filter( date__month__gte=month, date__month__lt=str(int(month)+1), date__year__gte=year, date__year__lt=str(int(year)+1))

        series = Series.objects.all()

        serializer = SeriesSerializer(series, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

        # response["Access-Control-Allow-Origin"] = "*"
        # response["Access-Control-Allow-Methods"] = "GET, POST"
        # response["Access-Control-Max-Age"] = "1000"
        # response["Access-Control-Allow-Headers"] = "year, month, Content-Type"

        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        data = {
            'round': request.data.get('round'),
            'forPlayoffs': request.data.get('forPlayoffs')
        }
        serializer = SeriesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DivisionApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the monthly sales of the department
        '''
        # print(request.META)

        # if request.META.get("HTTP_YEAR") is None or request.META.get("HTTP_MONTH") is None:
        #     playoffs = Playoff.objects.all()
        # else:
        #     year = request.META.get("HTTP_YEAR")
        #     month = request.META.get("HTTP_MONTH")
        #     domestics = Domestic.objects.filter( date__month__gte=month, date__month__lt=str(int(month)+1), date__year__gte=year, date__year__lt=str(int(year)+1))

        division = Division.objects.all()

        serializer = DivisionSerializer(division, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

        # response["Access-Control-Allow-Origin"] = "*"
        # response["Access-Control-Allow-Methods"] = "GET, POST"
        # response["Access-Control-Max-Age"] = "1000"
        # response["Access-Control-Allow-Headers"] = "year, month, Content-Type"

        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        data = {
            'forConference': request.data.get('forConference'),
            'name': request.data.get('name')
        }
        serializer = SeriesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StadiumApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the monthly sales of the department
        '''
        # print(request.META)

        # if request.META.get("HTTP_YEAR") is None or request.META.get("HTTP_MONTH") is None:
        #     playoffs = Playoff.objects.all()
        # else:
        #     year = request.META.get("HTTP_YEAR")
        #     month = request.META.get("HTTP_MONTH")
        #     domestics = Domestic.objects.filter( date__month__gte=month, date__month__lt=str(int(month)+1), date__year__gte=year, date__year__lt=str(int(year)+1))

        stadium = Stadium.objects.all()

        serializer = StadiumSerializer(stadium, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

        # response["Access-Control-Allow-Origin"] = "*"
        # response["Access-Control-Allow-Methods"] = "GET, POST"
        # response["Access-Control-Max-Age"] = "1000"
        # response["Access-Control-Allow-Headers"] = "year, month, Content-Type"

        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        data = {
            'location': request.data.get('location'),
            'name': request.data.get('name'),
            'capacity': request.data.get('capacity')
        }
        serializer = SeriesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TeamApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the monthly sales of the department
        '''
        # print(request.META)

        # if request.META.get("HTTP_YEAR") is None or request.META.get("HTTP_MONTH") is None:
        #     playoffs = Playoff.objects.all()
        # else:
        #     year = request.META.get("HTTP_YEAR")
        #     month = request.META.get("HTTP_MONTH")
        #     domestics = Domestic.objects.filter( date__month__gte=month, date__month__lt=str(int(month)+1), date__year__gte=year, date__year__lt=str(int(year)+1))

        team = Team.objects.all()

        serializer = TeamSerializer(team, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

        # response["Access-Control-Allow-Origin"] = "*"
        # response["Access-Control-Allow-Methods"] = "GET, POST"
        # response["Access-Control-Max-Age"] = "1000"
        # response["Access-Control-Allow-Headers"] = "year, month, Content-Type"

        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        data = {
            'inDivision': request.data.get('inDivision'),
            'name': request.data.get('name'),
            'titlesWon': request.data.get('titlesWon'),
            'gamesWon': request.data.get('capacity'),
            'gamesLost': request.data.get('titlesLost'),
            'dateFounded': request.data.get('dateFounded'),
            'fans': request.data.get('fans'),
            'sponsors': request.data.get('sponsors'),
            'logo': request.data.get('logo'),
            'hasStadium': request.data.get('hasStadium'),
            #missing coach
        }
        serializer = SeriesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PlayerApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the monthly sales of the department
        '''
        # print(request.META)

        # if request.META.get("HTTP_YEAR") is None or request.META.get("HTTP_MONTH") is None:
        #     playoffs = Playoff.objects.all()
        # else:
        #     year = request.META.get("HTTP_YEAR")
        #     month = request.META.get("HTTP_MONTH")
        #     domestics = Domestic.objects.filter( date__month__gte=month, date__month__lt=str(int(month)+1), date__year__gte=year, date__year__lt=str(int(year)+1))

        player = Player.objects.all()

        serializer = PlayerSerializer(player, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

        # response["Access-Control-Allow-Origin"] = "*"
        # response["Access-Control-Allow-Methods"] = "GET, POST"
        # response["Access-Control-Max-Age"] = "1000"
        # response["Access-Control-Allow-Headers"] = "year, month, Content-Type"

        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        data = {
            'inTeam': request.data.get('inTeam'),
            'fullName': request.data.get('fullName'),
            'position': request.data.get('position'),
            'age': request.data.get('age'),
            'nationality': request.data.get('nationality'),
            'university': request.data.get('university'),
            'height': request.data.get('height'),
            'weight': request.data.get('weight'),
            'agent': request.data.get('agent'),
            'pointsScored': request.data.get('pointsScored'),
            'rebounds': request.data.get('rebounds'),
            'steals': request.data.get('steals'),
            'turnovers': request.data.get('turnovers'),
        }
        serializer = PlayerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GameApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the monthly sales of the department
        '''
        # print(request.META)

        # if request.META.get("HTTP_YEAR") is None or request.META.get("HTTP_MONTH") is None:
        #     playoffs = Playoff.objects.all()
        # else:
        #     year = request.META.get("HTTP_YEAR")
        #     month = request.META.get("HTTP_MONTH")
        #     domestics = Domestic.objects.filter( date__month__gte=month, date__month__lt=str(int(month)+1), date__year__gte=year, date__year__lt=str(int(year)+1))

        game = Game.objects.all()

        serializer = GameSerializer(game, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

        # response["Access-Control-Allow-Origin"] = "*"
        # response["Access-Control-Allow-Methods"] = "GET, POST"
        # response["Access-Control-Max-Age"] = "1000"
        # response["Access-Control-Allow-Headers"] = "year, month, Content-Type"

        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        data = {
            'date': request.data.get('date'),
            'winner': request.data.get('winner'),
            'mvp': request.data.get('mvp'),
            'inSeries': request.data.get('inSeries'),
            'gameNumber': request.data.get('gameNumber'),
            'highlights': request.data.get('highlights'),
            'home': request.data.get('home'),
            'away': request.data.get('away'),
            'homeScore': request.data.get('homeScore'),
            'homeRebounds': request.data.get('homeRebounds'),
            'homeSteals': request.data.get('homeSteals'),
            'homeTurnovers': request.data.get('homeTurnovers'),
            'homeTimeouts': request.data.get('homeTimeouts'),
            'homeFouls': request.data.get('homeFouls'),
            'homeShotAttempts': request.data.get('homeShotAttempts'),
            'awayScore': request.data.get('awayScore'),
            'awayRebounds': request.data.get('awayRebounds'),
            'awaySteals': request.data.get('awaySteals'),
            'awayTurnovers': request.data.get('awayTurnovers'),
            'awayTimeouts': request.data.get('awayTimeouts'),
            'awayFouls': request.data.get('awayFouls'),
            'awayShotAttempts': request.data.get('awayShotAttempts'),
        }
        serializer = GameSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
