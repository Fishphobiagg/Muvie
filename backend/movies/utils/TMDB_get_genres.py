import requests
import json

def get_movie_genres():
    url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {
        "api_key": "84216c3a0ee24447b6798e642dbfa540",  # 자신의 TMDB API 키로 바꿔주세요
        "language": "ko-KR",
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    return data

def transform_genre_data(genre):
    transformed_genre = {
        "model": "movies.genre",
        "id": genre["id"],
        "fields": {
            "name": genre["name"]
        }
    }
    
    return transformed_genre

def save_genres_to_fixture(genres):
    transformed_genres = [transform_genre_data(genre) for genre in genres["genres"]]
    filename = "../fixtures/genres.json"
    
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(transformed_genres, file, ensure_ascii=False, indent=4)

genres = get_movie_genres()
save_genres_to_fixture(genres)