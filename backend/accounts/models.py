from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from musics .models import MusicComponent, Music

class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')
        nickname = kwargs.get('nickname', '')
        user = self.model(
            email=email,
            nickname=nickname,
            profile_picture = kwargs.get('profile_picture', '')
        )
        user.set_password(password)
        user.save(using=self._db)

        music_component = MusicComponent.objects.create(
            energy=0.5,
            instrumentalness=0.5,
            liveness=0.5,
            acousticness=0.5,
            speechiness=0.5,
            valence=0.5,
            tempo=80,
            mode=0.5,
            loudness=50,
            danceability=0.5,
        )
        
        # MusicComponent와 User의 관계 설정
        user.music_components = music_component
        user.save()
        # vector 값 계산
        return user
    


# AbstractBaseUser를 상속해서 유저 커스텀
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    profile_picture = models.ImageField(blank=True, null=True, upload_to='users')
    nickname = models.CharField(max_length=20, unique=True, null=True, blank=True)
    following = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='followers')
    music_components = models.OneToOneField(MusicComponent, on_delete=models.CASCADE, blank=True, null=True)
    playlist = models.ManyToManyField(Music, blank=True)
    like_music = models.ManyToManyField(Music, blank=True, related_name="users_like_musics", through='MusicUserLike')
	# 헬퍼 클래스 사용
    objects = UserManager()
	# 사용자의 username field는 email으로 설정 (이메일로 로그인)
    USERNAME_FIELD = 'email'

class MusicUserLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)