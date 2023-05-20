from django.urls import path
from . import views

urlpatterns = [
    path('ost', views.save_ost),
    path('<int:movie_pk>/ost', views.search_movie_ost),
    path('search/<keyword>', views.search_movie),
    path('data', views.save_ost),
]