import requests
from bs4 import BeautifulSoup
from ...models import Music
from django.core.management.base import BaseCommand
from pprint import pprint

class Command(BaseCommand):
    help = 'Fetches YouTube video links for existing Music objects'

    def handle(self, *args, **options):
        def get_youtube_video_id(title, artist):
            # YouTube에서 동영상 검색 및 가장 위에 뜨는 동영상의 video id 가져오기
            search_url = f'https://www.youtube.com/results?search_query={title}+{artist}'
            response = requests.get(search_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            print(soup)

            # Extract the video_id from the href attribute of the anchor tag
            script = soup.find('script', {'type': 'application/ld+json'})
            print(script)
            # Extract the JSON data from the script element
            json_data = script.string
            print(json_data)
            # Find the index of 'watchEndpoint' in the JSON data
            watch_endpoint_index = json_data.find('watchEndpoint')
            print(watch_endpoint_index)
            return None
            video_id = soup.find('a')['href']
            print(video_id)
            if video_id:
                print(video_id)
                return None
        # 기존 Music 객체들에 YouTube 동영상 링크 저장
        music_objects = Music.objects.all()
        for music in music_objects:
            if not music.video_id:
                video_id = get_youtube_video_id(music.title, music.artist)
                if video_id:
                    music.video_id = video_id
                    music.save()
                    print(music.pk, music.video_id)
                    