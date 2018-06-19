from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('who', views.who, name='who'),
    path('<int:course_id>', views.detail, name='detail2'),
]
