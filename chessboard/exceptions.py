class InvalidMoveError(Exception):
    """Выбрасывается, когда игрок делает неверный ход"""

    def __init__(self, move, message=None):
        if message is None:
            message = f"Неверный ход: {move}"
        self.move = move
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"[InvalidMoveError] {self.message}"