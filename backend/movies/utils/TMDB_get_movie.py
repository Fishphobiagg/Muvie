import requests
import json
from django.conf import settings

def get_popular_movies():
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": '84216c3a0ee24447b6798e642dbfa540',  # 자신의 TMDB API 키로 바꿔주세요
        "sort_by": "popularity.desc",
        "vote_count.gte": 100,
        "language":"ko-KR",
        "page": 1
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    movies = []
    for page in range(1, 50):
        params["page"] = page
        response = requests.get(url, params=params)
        data = response.json()

        if "results" in data:
            movies.extend(data["results"])
        else:
            break
        print(page)
        page += 1
    
    return movies[:10000]
 
def transform_movie_data(movie):
    transformed_movie = {
        "model": "movies.movie",
        "fields": {
            "title": movie["title"],
            "original_title": movie["original_title"],
            "release_date": movie["release_date"],
            "popularity": movie["popularity"],
            "vote_count": movie["vote_count"],
            "vote_average": movie["vote_average"],
            "overview": movie["overview"],
        }
    }
    return transformed_movie

def save_movies_to_fixture(movies):
    transformed_movies = [transform_movie_data(movie) for movie in movies]
    filename = "../fixtures/movies.json"
    
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(transformed_movies, file, ensure_ascii=False, indent=4)

movies = get_popular_movies()
save_movies_to_fixture(movies)