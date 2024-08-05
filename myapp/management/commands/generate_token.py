from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Generate tokens for all users'

    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            token, created = Token.objects.get_or_create(user=user)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Token created for user {user.username}'))
            else:
                self.stdout.write(self.style.WARNING(f'Token already exists for user {user.username}'))
