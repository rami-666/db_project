from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import (
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
)  #add models here 


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = "__all__"

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
        fields = ["inDivision", "name", "titlesWon", "gamesWon", "gamesLost", "dateFounded", "fans", "sponsors", "logo", "hasStadium"]


class Team_CoachSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Team_Coach
        fields = ["team", "coach", "date"]


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["fullName", "position", "age", "nationality", "university", "height", "weight", "agent", "pointsScored", "rebounds", "steals", "turnovers", "image"]

class Team_PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team_Player
        fields = ["team", "player", "date"]


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["date", "winner", "mvp", "inSeries", "gameNumber", "highlights", "home", "away", "homeScore", "homeRebounds", "homeSteals", "homeTurnovers", "homeTimeouts", "homeFouls", "homeShotAttempts", "awayScore", "awayRebounds", "awaySteals", "awayTurnovers", "awayTimeouts", "awayFouls", "awayShotAttempts", "inSeason"]

class Game_PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game_Player
        fields = ["game", "player", "score", "rebounds", "steals", "turnovers", "fouls", "shotAttempts"]


class ScoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scout
        fields = ["name", "university"]


class Team_ScoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team_Scout
        fields = ["team", "scout", "date"]


class RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = ["name", "position"]


class Game_RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game_Referee
        fields = ["game", "referee"]
