from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Dump data for User, Music, and related tables.'
    def handle(self, *args, **options):
        # 데이터를 덤프할 파일 경로
        dump_file = os.path.join(os.getcwd(), 'data_dump.json')

        dump_file = 'data_dump.json'

        # User, Music, MusicComponent, Movie, MusicUserLike, MovieUserLike 모델과 관련된 테이블 데이터를 덤프
        call_command('dumpdata', 'accounts.user', 'musics.music', 'musics.musiccomponent', 'movies.movie', 'movies.movie_ost', 'accounts.user_playlist', 'accounts.user_following', 'accounts.musicuserlike', '--natural-foreign', '--natural-primary', '--output', dump_file)

        self.stdout.write(self.style.SUCCESS(f"Data dumped to {dump_file}"))