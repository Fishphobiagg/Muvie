from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Dump all database data while preserving relationships'

    def handle(self, *args, **options):
        # 데이터를 덤프할 파일 경로
        dump_file = os.path.join(os.getcwd(), 'data_dump.json')

        # 데이터를 덤프할 앱 이름 목록
        app_names = ['accounts', 'musics', 'movies']

        # 모든 앱의 데이터를 덤프
        call_command('dumpdata', *app_names, '--natural-foreign', '--natural-primary', '--output', dump_file)

        self.stdout.write(self.style.SUCCESS(f"Data dumped to {dump_file}"))
