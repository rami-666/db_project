from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import (
Playoff,
Conference,
Series, 
Division, 
Stadium, 
Coach,
Team, 
Player, 
Game,
Game_Player,
Scout,
Referee,
Game_Referee
)  #add models here 



class PlayoffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playoff
        fields =["season"]

class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields =["name", "hasPlayoffs"]

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ["round", "forPlayoffs"]

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ["forConference", "name"]

class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ["location", "name", "capacity"]

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ["name", "position", "age", "yearsOfCoaching", "university", "nationality"]

class TeamSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Team
        fields = ["inDivision", "name", "titlesWon", "gamesWon", "gamesLost", "dateFounded", "fans", "sponsors", "logo", "hasStadium", "coach"]


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["inTeam", "fullName", "position", "age", "nationality", "university", "height", "weight", "agent", "pointsScored", "rebounds", "steals", "turnovers"]


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["date", "winner", "mvp", "inSeries", "gameNumber", "highlights", "home", "away", "homeScore", "homeRebounds", "homeSteals", "homeTurnovers", "homeTimeouts", "homeFouls", "homeShotAttempts", "awayScore", "awayRebounds", "awaySteals", "awayTurnovers", "awayTimeouts", "awayFouls", "awayShotAttempts"]

class Game_PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game_Player
        fields = ["game", "player", "score", "rebounds", "steals", "turnovers", "fouls", "shotAttempts"]


class ScoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scout
        fields = ["name", "university", "forTeam"]


class RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = ["name", "position"]


class Game_RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game_Referee
        fields = ["game", "referee"]
