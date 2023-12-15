import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.environ.get('SU_EMAIL'),
            first_name='NN',
            last_name='UU',
            telegram=f"{os.environ.get('SU_TELEGRAM')}",
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(f"{os.environ.get('SU_PASSWORD')}")
        user.save()
