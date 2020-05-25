from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    # ex: /polls/5/results/
    path('register/', views.register, name='register'),
    # ex: /polls/5/vote/
    path('publish/', views.publishBlog, name='publishBlog'),
    path('logout/', views.login, name='loginout'),
    path('comment/', views.comment, name='comment'),
    path('reply/', views.reply, name='reply'),
]