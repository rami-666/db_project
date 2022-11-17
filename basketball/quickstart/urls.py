from django.urls import re_path as url
from django.urls import path, include
from .views import (
PlayoffApiView,
ConferenceApiView,
SeriesApiView,
DivisionApiView,
StadiumApiView,
TeamApiView,
PlayerApiView,
GameApiView
)

urlpatterns = [
    path('playoff', PlayoffApiView.as_view()),
    path('conference',ConferenceApiView.as_view()),
    path('series',SeriesApiView.as_view()),
    path('division',DivisionApiView.as_view()),
    path('stadium',StadiumApiView.as_view()),
    path('team', TeamApiView.as_view()),
    path('player', PlayerApiView.as_view()),
    path('game', GameApiView.as_view()),
]