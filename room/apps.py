from django.apps import AppConfig
from django.db.utils import OperationalError

class RoomConfig(AppConfig):
    name = 'room'

    def ready(self):
        try:
            from .views import initialize_rooms_without_request
            initialize_rooms_without_request()
        except OperationalError:
            pass
