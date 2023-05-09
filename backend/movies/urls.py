from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_movies),
    path('<int:movie_pk>', views.movie),
    path('<int:movie_pk>/like', views.user_movie_like),
    path('<int:movie_pk>/ost', views.search_movie_ost),
    path('search/<keyword>', views.search_movie),
]
