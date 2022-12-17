import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import views
from .models import (           #add models here
Season,
Playoff,
Conference,
Series, 
Division, 
Stadium, 
Coach,
Team, 
Team_Coach,
Player,
Team_Player,
Game,
Game_Player,
Scout,
Team_Scout,
Referee,
Game_Referee
)  
from .serializers import (      #add  seiralizers here
SeasonSerializer,
PlayoffSerializer, 
ConferenceSerializer, 
SeriesSerializer, 
DivisionSerializer, 
StadiumSerializer, 
CoachSerializer,
TeamSerializer, 
Team_CoachSerializer,
PlayerSerializer,
Team_PlayerSerializer,
GameSerializer,
Game_PlayerSerializer,
ScoutSerializer,
Team_ScoutSerializer,
RefereeSerializer,
Game_RefereeSerializer
)  


# Create your views here.
class SeasonApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
         
        '''
 
        season = Season.objects.all()

        serializer = SeasonSerializer(season, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        data = {
            'year': request.data.get('year'),
            'numberOfGames': request.data.get('numberOfGames')
        }
        serializer = SeasonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlayoffApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
         
        '''
 
        playoffs = Playoff.objects.all()

        serializer = PlayoffSerializer(playoffs, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
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
         
        '''
 
        conferences = Conference.objects.all()

        serializer = ConferenceSerializer(conferences, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
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
         
        '''
 
        series = Series.objects.all()

        serializer = SeriesSerializer(series, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
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
         
        '''
 
        division = Division.objects.all()

        serializer = DivisionSerializer(division, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
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
        serializer = DivisionSerializer(data=data)
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
         
        '''
 
        stadium = Stadium.objects.all()

        serializer = StadiumSerializer(stadium, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
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
        serializer = StadiumSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CoachApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
         
        '''
 
        coach = Coach.objects.all()

        serializer = CoachSerializer(coach, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        data = {
            'name': request.data.get('name'),
            'position': request.data.get('position'),
            'age': request.data.get('age'),
            'yearsOfCoaching': request.data.get('yearsOfCoaching'),
            'university': request.data.get('university'),
            'nationality': request.data.get('nationality')
        }
        serializer = CoachSerializer(data=data)
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
         
        '''
 
        team = Team.objects.all()

        serializer = TeamSerializer(team, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
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
            'gamesWon': request.data.get('gamesWon'),
            'gamesLost': request.data.get('gamesLost'),
            'dateFounded': request.data.get('dateFounded'),
            'fans': request.data.get('fans'),
            'sponsors': request.data.get('sponsors'),
            'logo': request.data.get('logo'),
            'hasStadium': request.data.get('hasStadium'),
            # 'coach': request.data.get('coach'),
        }
        serializer = TeamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Team_CoachApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
         
        '''
 
        team_coach = Team_Coach.objects.all()

        serializer = Team_CoachSerializer(team_coach, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        data = {
            'team': request.data.get('team'),
            'coach': request.data.get('coach'),
            'date': request.data.get('date'),
        }
        serializer = Team_CoachSerializer(data=data)
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
         
        '''
 
        player = Player.objects.all()

        serializer = PlayerSerializer(player, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        print("TYPE: " + str(type(request.data)))
        data = {
            # 'inTeam': request.data.get('inTeam'),
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
            'image': request.data.get('image')
        }
        serializer = PlayerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Team_PlayerApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
         
        '''
 
        team_player = Team_Player.objects.all()

        serializer = Team_PlayerSerializer(team_player, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        data = {
            'team': request.data.get('team'),
            'player': request.data.get('player'),
            'date': request.data.get('date'),
        }
        serializer = Team_PlayerSerializer(data=data)
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
         
        '''
 
        game = Game.objects.all()

        serializer = GameSerializer(game, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
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
            'inSeason': request.data.get('inSeason'),
        }
        serializer = GameSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Game_PlayerApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
         
        '''
 
        game_player = Game_Player.objects.all()

        serializer = Game_PlayerSerializer(game_player, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        data = {
            'game': request.data.get('game'),
            'player': request.data.get('player'),
            'score': request.data.get('score'),
            'rebounds': request.data.get('rebounds'),
            'steals': request.data.get('steals'),
            'turnovers': request.data.get('turnovers'),
            'fouls': request.data.get('fouls'),
            'shotAttempts': request.data.get('shotAttempts'),
            
        }
        serializer = Game_PlayerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScoutApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
         
        '''
 
        scout = Scout.objects.all()

        serializer = ScoutSerializer(scout, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        data = {
            'name': request.data.get('name'),
            'university': request.data.get('university'),
            # 'forTeam': request.data.get('forTeam'),
        }
        serializer = ScoutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Team_ScoutApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
         
        '''
 
        team_scout = Team_Scout.objects.all()

        serializer = Team_ScoutSerializer(team_scout, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        data = {
            'team': request.data.get('team'),
            'scout': request.data.get('scout'),
            'date': request.data.get('date'),
        }
        serializer = Team_ScoutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RefereeApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
         
        '''
 
        referee = Referee.objects.all()

        serializer = RefereeSerializer(referee, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        data = {
            'name': request.data.get('name'),
            'position': request.data.get('position'),
        }
        serializer = RefereeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Game_RefereeApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
         
        '''
 
        game_referee = Game_Referee.objects.all()

        serializer = Game_RefereeSerializer(game_referee, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
        return response


    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print(request.data)
        data = {
            'game': request.data.get('game'),
            'referee': request.data.get('referee'),
        }
        serializer = Game_RefereeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# test view

class TeamFilterApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]



    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
         
        '''

        body = request.data.get("team")
        teams = Team.objects.filter(name=body)

        serializer = TeamSerializer(teams, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

 
        return response


    