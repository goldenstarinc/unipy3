from django.contrib import admin
from django.urls import path
from chessboard.views import ChessGameView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', ChessGameView.as_view(), name='chess_game'),
]