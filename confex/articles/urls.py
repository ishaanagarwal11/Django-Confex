from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.article_create, name='create'),
    path('my_articles/', views.my_articles, name='my_articles'),
    path('<slug:slug>/', views.article_detail, name='detail'),
    path('delete/<slug:slug>/', views.delete_article, name='delete'),  # Add this line
 
]
