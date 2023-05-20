from django.core.management.base import BaseCommand
import random
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Make users follow random users'

    def handle(self, *args, **options):
        # 모든 유저 조회
        all_users = User.objects.all()

        # 각 유저마다 무작위로 100명씩 팔로우
        for user in all_users:
            # 자기 자신을 제외한 모든 유저들을 리스트로 생성
            other_users = list(all_users.exclude(id=user.id))
            # 무작위로 100명 선택
            random_users = random.sample(other_users, k=100)
            # 팔로우 추가
            user.following.add(*random_users)

        self.stdout.write(self.style.SUCCESS('Successfully made users follow random users'))
