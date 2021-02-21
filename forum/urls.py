from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_main, name='forum_main'),
    path('create_forum/', views.create_forum, name='create_forum'),
    path('addInDiscussion/', views.addInDiscussion, name='addInDiscussion'),
]