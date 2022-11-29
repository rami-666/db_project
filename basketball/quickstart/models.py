from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Season(models.Model):
    year = models.IntegerField(unique = True)
    numberOfGames = models.IntegerField()

    def __str__(self):
        return str(self.year)




class Playoff(models.Model):
    season = models.IntegerField(unique=True)

    def __str__(self):
        return  str(self.season)

class Conference(models.Model):
    name = models.CharField(max_length=100)
    hasPlayoffs = models.ForeignKey(Playoff, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name + ": " + str(self.hasPlayoffs)


class Series(models.Model):
    round = models.IntegerField()
    forPlayoffs = models.ForeignKey(Playoff, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "Round: " + str(self.round) + " Playoffs: " + str(self.forPlayoffs)


class Division(models.Model):
    forConference = models.ForeignKey(Conference, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " for Conference: " + str(self.forConference)

class Stadium(models.Model):
    location = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Coach(models.Model):
    name = models.CharField(max_length=300)
    position = models.CharField(max_length=10)
    age = models.IntegerField()
    yearsOfCoaching = models.IntegerField()
    university = models.CharField(max_length=200)
    nationality = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Team(models.Model):
    inDivision = models.ForeignKey(Division, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    titlesWon = models.IntegerField()
    gamesWon = models.IntegerField()
    gamesLost = models.IntegerField()
    dateFounded = models.DateField()
    fans = models.IntegerField()
    sponsors = models.IntegerField()
    logo  = models.CharField(max_length=1000)
    hasStadium = models.ForeignKey(Stadium, on_delete= models.DO_NOTHING)
    # coach = models.ForeignKey(Coach, on_delete= models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name

class Team_Coach(models.Model):
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    coach = models.ForeignKey(Coach, on_delete=models.DO_NOTHING)
    date = models.DateField()

    def __str__(self):
        return str(self.team) + " : " + str(self.coach)

class Player(models.Model):
    # inTeam = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    fullName = models.CharField(max_length=100)
    position = models.CharField(max_length=10)
    age = models.IntegerField()
    nationality = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    agent = models.CharField(max_length=100)
    pointsScored = models.IntegerField()
    rebounds = models.IntegerField()
    steals = models.IntegerField()
    turnovers = models.IntegerField()

    def __str__(self):
        return self.fullName

class Team_Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    player = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    date = models.DateField()

    def __str__(self):
        return str(self.team) + " " + str(self.player)

class Game(models.Model):
    date = models.DateField()
    winner = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="winner") #check if necessary to have foreign key
    mvp = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    inSeries = models.ForeignKey(Series, on_delete=models.DO_NOTHING)
    gameNumber = models.IntegerField()
    highlights = models.CharField(max_length=1000)
    home = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="home")
    away = models.ForeignKey(Team, models.DO_NOTHING, related_name="away")
    homeScore = models.IntegerField()
    homeRebounds = models.IntegerField()
    homeSteals = models.IntegerField()
    homeTurnovers = models.IntegerField()
    homeTimeouts = models.IntegerField()
    homeFouls = models.IntegerField()
    homeShotAttempts = models.IntegerField()
    awayScore = models.IntegerField()
    awayRebounds = models.IntegerField()
    awaySteals = models.IntegerField()
    awayTurnovers = models.IntegerField()
    awayTimeouts = models.IntegerField()
    awayFouls = models.IntegerField()
    awayShotAttempts = models.IntegerField()
    inSeason = models.ForeignKey(Season, on_delete=models.DO_NOTHING, null = True)

    def __str__(self):
        return str(self.home) + " vs. " + str(self.away)


class Game_Player(models.Model):
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    player = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    score = models.IntegerField()
    rebounds = models.IntegerField()
    steals = models.IntegerField()
    turnovers = models.IntegerField()
    fouls = models.IntegerField()
    shotAttempts = models.IntegerField()

    def __str__(self):
        return str(self.game) + " - " + str(self.player)


class Scout(models.Model):
    name = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    # forTeam = models.ForeignKey(Team, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Team_Scout(models.Model):
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    scout = models.ForeignKey(Scout, on_delete=models.DO_NOTHING)
    date = models.DateField()

    def __str__(self):
        return str(self.team) + " : " + str(self.scout)

class Referee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game_Referee(models.Model):
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    referee = models.ForeignKey(Referee, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.game) + " : " + str(self.referee)


    
