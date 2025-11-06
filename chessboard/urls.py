from django.urls import path
from .views import ChessGameView

urlpatterns = [
    path('', ChessGameView.as_view(), name='chess_game'),
]