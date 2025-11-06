from django.shortcuts import render
from django.http import JsonResponse
from .models import Game
import chess

def index(request):
    game, _ = Game.objects.get_or_create(id=1)
    board = chess.Board() if game.fen == "startpos" else chess.Board(game.fen)

    if request.method == "POST":
        move = request.POST.get("move")
        try:
            board.push_san(move)
            game.fen = board.fen()
            game.turn = "white" if board.turn else "black"
            game.save()
            return JsonResponse({"valid": True, "fen": game.fen})
        except:
            return JsonResponse({"valid": False, "fen_before": game.fen})

    return render(request, "chessboard/game.html", {"turn": game.turn, "fen": game.fen})
