from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from book_visualizer import api_to_db

class Command(BaseCommand):
    help = "Requests categories from NYT"

    def handle(self, *args, **options):
        try:
            api_to_db.update_list_names()
        except KeyError:
            pass