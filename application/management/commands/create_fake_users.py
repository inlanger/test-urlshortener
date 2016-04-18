import requests

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


def get_random_user(results=10):
    return requests.get(
        'http://api.randomuser.me/',
        params={'format': 'json', 'results': results}
    ).json()['results']


class Command(BaseCommand):
    help = 'Creates fake users'

    def add_arguments(self, parser):
        parser.add_argument('results', nargs='+', type=int)

    def handle(self, *args, **options):
        if options['results'][0] > 0:

            self.stdout.write('Starting generation...')

            for user in get_random_user(options['results'][0]):

                # We could use bulk_create for optimization.
                User.objects.create_user(
                    username=user['login']['username'],
                    email=user['email'],
                    password=user['login']['password'],
                    first_name=user['name']['first'],
                    last_name=user['name']['last'],
                )

                self.stdout.write(
                    'User {} was generated.'.format(user['login']['username'])
                )
        else:
            self.stdout.write(self.style.ERROR(
                'You have to specify count of fake users to created.'
            ))
