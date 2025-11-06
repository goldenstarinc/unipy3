from django.apps import AppConfig

# Класс конфигурации приложения.
# Django использует его для регистрации приложения и инициализации при запуске сервера.

class ChessboardConfig(AppConfig):
    # Указывает тип поля, используемого по умолчанию для первичных ключей (id)
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chessboard'
