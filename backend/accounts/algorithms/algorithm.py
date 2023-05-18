import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from ..models import User
from sklearn.preprocessing import StandardScaler


def recommend_ost(components):
    sp_client_id = '150e34294220415f8bc1337af12adb58'
    sp_secret = '257cf688a26f4c8181c2b3b5447ac4e1'
    sp_client_credentials_manager = SpotifyClientCredentials(client_id=sp_client_id, client_secret=sp_secret)
    sp = spotipy.Spotify(client_credentials_manager=sp_client_credentials_manager)
    user_features = [
    float(components['energy']),
    float(components['instrumentalness']),
    float(components['liveness']),
    float(components['acousticness']),
    float(components['speechiness']),
    float(components['valence']),
    float(components['tempo']),
    float(components['mode']),
    float(components['loudness']),
    float(components['danceability'])
    ]
    seed_features = [round(num, 3) for num in user_features]
    recommendations = sp.recommendations(seed_genres=['movies'],market='KR',seed_features=seed_features, limit=10)
    return recommendations

def recommend_simillar_user(components):
    pass

def recommend_by_like(like_list):
    pass

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

    return normalized_vector