from django.urls import path
from . import views

urlpatterns = [
	path('', views.home , name = 'home'),
	path('<int:article_id>/' , views.articlePage , name = 'articlePage'),
	path('index/' , views.index, name = 'index'),
]