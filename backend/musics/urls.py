from django.urls import path
from . import views


urlpatterns = [
      path('', views.music),
    #   path('playlist/<int:music_pk>', views.) 
]