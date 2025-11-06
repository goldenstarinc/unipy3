from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from .models import Game
from .exceptions import InvalidMoveError
import chess
import logging

logger = logging.getLogger('chessboard')


class ChessGameView(View):
    template_name = "chessboard/game.html"

    def get(self, request):
        # Создаём или берём игру
        game, _ = Game.objects.get_or_create(id=1)
        # Если fen пустой — начинаем новую партию
        if not game.fen or game.fen == "startpos":
            board = chess.Board()
            game.fen = board.fen()
            game.turn = "white"
            game.save()

        logger.info("Загружена страница игры. Текущий ход: %s", game.turn)
        return render(request, self.template_name, {
            "turn": game.turn,
            "fen": game.fen
        })

    def post(self, request):
        game, _ = Game.objects.get_or_create(id=1)
        board = chess.Board() if game.fen == "startpos" else chess.Board(game.fen)

        action = request.POST.get("action")
        move = request.POST.get("move")

        # Reset
        if action == "reset":
            board.reset()
            game.fen = board.fen()
            game.turn = "white"
            game.save()
            logger.info("♻️ Игра сброшена пользователем.")
            return JsonResponse({"reset": True, "fen": game.fen})

        # Обычный ход
        if not move:
            return JsonResponse({"valid": False, "error": "Ход не получен"})

        try:
            board.push_san(move)
            game.fen = board.fen()
            game.turn = "white" if board.turn else "black"
            game.save()
            logger.info("Ход %s выполнен. Следующий ход: %s", move, game.turn)
            return JsonResponse({"valid": True, "fen": game.fen, "turn": game.turn})
        except Exception as e:
            logger.warning("Ошибка при ходе %s: %s", move, str(e))
            raise InvalidMoveError(f"Неверный ход: {move}")
