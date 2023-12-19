from users.models import User
from django.core.management import BaseCommand
import os, dotenv

dotenv.load_dotenv()


class Command(BaseCommand):
    """
    Custom management command to create or update the superuser with admin privileges.
    """

    def handle(self, *args, **kwargs):
        user, just_created = User.objects.get_or_create(
            email=os.getenv("ADMIN_EMAIL"),
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(os.getenv("ADMIN_PASSWORD"))
        user.save()
