from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from musics .models import MusicComponent, Music
from movies .models import Movie
from sklearn.preprocessing import StandardScaler

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
        user.calculate_vector()
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

    def calculate_vector(self):
        scaler = StandardScaler()
        # MusicComponent의 필드 값을 가져옴
        normalized_vector = scaler.fit_transform([
    [self.music_components.energy],
    [self.music_components.instrumentalness],
    [self.music_components.liveness],
    [self.music_components.speechiness],
    [self.music_components.acousticness],
    [self.music_components.valence],
    [self.music_components.tempo*0.1],
    [self.music_components.mode],
    [self.music_components.loudness*0.1],
    [self.music_components.danceability],
])

        vector = normalized_vector
        # 계산된 값을 vector 필드에 저장
        self.music_components.vector = vector
        self.music_components.save()

class MovieUserLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class MusicUserLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)