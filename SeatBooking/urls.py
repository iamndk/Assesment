from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('home/', views.index, name='index'),
     path('signup/', views.signup, name='signup'),
     path('movie_list/', views.movie_list, name='movie_list'),

      path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('book/<int:pk>/', views.book_ticket, name='book_ticket'),
]