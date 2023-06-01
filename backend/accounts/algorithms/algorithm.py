import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings
from ..models import User, MusicUserLike
from musics.models import Music
import random
from django.db.models import Count

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

def collaborative_filtering(user, n=10):
    liked_music_ids = list(MusicUserLike.objects.filter(user=user).order_by('-created_at').values_list('music_id', flat=True)[:10])

    if not liked_music_ids:
        liked_music_ids = list(Music.objects.order_by('?').values_list('id', flat=True)[:10])
    elif len(liked_music_ids) < 10:
        other_query = list(Music.objects.order_by('?').values_list('id', flat=True)[:10 - len(liked_music_ids)])
        liked_music_ids.extend(other_query)
    similar_users = random.sample(list(User.objects.filter(musicuserlike__music_id__in=liked_music_ids)), 10)
    similarity_scores = {}
    for similar_user in similar_users:
        similar_user_liked_music_ids = MusicUserLike.objects.filter(user=similar_user).values_list('music_id')
        similarity_scores[similar_user.id] = len(set(liked_music_ids) & set(similar_user_liked_music_ids))
    sorted_similar_users = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)

    top_similar_users = [item[0] for item in sorted_similar_users[:n]]
    recommend_music = Music.objects.filter(musicuserlike__user__id__in=top_similar_users).annotate(like_count=Count('musicuserlike')).order_by('-like_count')

    return recommend_music, top_similar_users