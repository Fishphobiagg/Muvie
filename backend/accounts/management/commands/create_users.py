import random
from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model
from accounts.models import MusicUserLike

User = get_user_model()


class Command(BaseCommand):
    help = 'Create users with profile picture, playlist, and likes'

    def handle(self, *args, **options):
        # Create 500 users
        for i in range(500):
            email = f'user{i}@example.com'
            password = 'password123'
            nickname = f'User{i}'
            profile_picture = '/users/default.gif'

            # Create a user with default profile picture
            user = User.objects.create_user(email=email, password=password, nickname=nickname, profile_picture=profile_picture)

            # Add random music to the playlist
            music_pks = list(range(9168, 25194))
            random.shuffle(music_pks)
            playlist = music_pks[:30]
            user.playlist.add(*playlist)

            # Add random music to the liked songs
            liked_songs = music_pks[30:60]
            for song in liked_songs:
                MusicUserLike.objects.create(user=user, music_id=song)

            # Update user's music components with random values
            user.music_components.energy = random.uniform(0, 1)
            user.music_components.instrumentalness = random.uniform(0, 1)
            user.music_components.liveness = random.uniform(0, 1)
            user.music_components.acousticness = random.uniform(0, 1)
            user.music_components.speechiness = random.uniform(0, 1)
            user.music_components.valence = random.uniform(0, 1)
            user.music_components.tempo = random.randint(60, 180)
            user.music_components.mode = random.uniform(0, 1)
            user.music_components.loudness = random.uniform(-60, 0)
            user.music_components.danceability = random.uniform(0, 1)
            user.music_components.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully created user: {email}'))
