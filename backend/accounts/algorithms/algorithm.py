import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from sklearn.preprocessing import StandardScaler
from django.conf import settings

def recommend_ost(components):
    sp_client_id = settings.SPOTIFY_ID
    sp_secret = settings.SPOTIFY_SECRET
    sp_client_credentials_manager = SpotifyClientCredentials(client_id=sp_client_id, client_secret=sp_secret)
    sp = spotipy.Spotify(client_credentials_manager=sp_client_credentials_manager)
   
    recommendations = sp.recommendations(seed_genres=['movies'],
    target_valence=components['valence'],target_energy=components['energy'],
    target_liveness=components['liveness'], target_speechiness=components['speechiness'],
    target_tempo=int(components['tempo']),target_acousticness=components['acousticness'],
    target_loudness=-int(components['loudness']) ,target_danceability=components['danceability'],
    target_instrumentalness=components['instrumentalness'],limit=10)
    return recommendations

def calculate_vector(components):
    normalized_vector = [
        float(components.music_components.energy),
        float(components.music_components.instrumentalness),
        float(components.music_components.liveness),
        float(components.music_components.speechiness),
        float(components.music_components.acousticness),
        float(components.music_components.valence),
        float(components.music_components.tempo) * 0.01,
        float(components.music_components.loudness) * 0.01,
        float(components.music_components.danceability),
    ]

    return normalized_vector