from django.db import models

# Модели Django описывают структуру данных, которые хранятся в базе.
# Каждая модель автоматически создаёт таблицу в базе данных
class Game(models.Model):
    # FEN (Forsyth–Edwards Notation) — строка, описывающая текущее положение фигур на доске.
    fen = models.CharField(max_length=100, default="startpos")
    turn = models.CharField(max_length=5, default="white")
