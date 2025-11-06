from django.db import models

class Game(models.Model):
    fen = models.CharField(max_length=100, default="startpos")
    turn = models.CharField(max_length=5, default="white")
