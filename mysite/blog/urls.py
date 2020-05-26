from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('editBlog/', views.editBlog, name='editBlog'),
    path('logout/', views.logout, name='loginout'),
    path('userIndex/', views.userIndex, name='userIndex'),
    path('<int:blog_id>/', views.blogDetail, name='blogDetail'),
]