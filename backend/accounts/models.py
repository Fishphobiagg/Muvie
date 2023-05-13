from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from musics .models import MusicComponent, Music
from movies .models import Movie

# 헬퍼 클래스
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
    like_movie = models.ManyToManyField(Movie, blank=True, related_name='users_like_movies', through='MovieUserLike')
    
	# 헬퍼 클래스 사용
    objects = UserManager()
	# 사용자의 username field는 email으로 설정 (이메일로 로그인)
    USERNAME_FIELD = 'email'

class MovieUserLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class MusicUserLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)