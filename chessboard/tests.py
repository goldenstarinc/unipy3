from django.test import TestCase, Client
from django.urls import reverse
from .models import Game

class ChessGameViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("chess_game")

    def test_get_game_page(self):
        """Страница игры открывается и возвращает шаблон"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "chessboard/game.html")
        self.assertIn("fen", response.context)
        self.assertIn("turn", response.context)

    def test_post_move_invalid(self):
        """POST без хода возвращает ошибку"""
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"valid": False, "error": "Ход не получен"})

    def test_post_reset(self):
        """Сброс игры работает"""
        response = self.client.post(self.url, {"action": "reset"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("reset", data)
        self.assertTrue(data["reset"])
        self.assertIn("fen", data)

    def test_post_valid_move(self):
        """Простой ход e4 должен быть допустимым"""
        Game.objects.create(id=1, fen="startpos")
        response = self.client.post(self.url, {"move": "e4"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["valid"])
        self.assertIn("fen", data)
        self.assertIn("turn", data)
