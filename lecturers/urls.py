from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:lecturer_id>', views.detail, name='detail'),
    path('home', views.home, name='home'),
    path('<int:lecturer_id>/upvote', views.upvote, name='upvote'),
]
