from django.urls import path
from . import views

urlpatterns = [
	path('', views.home , name = 'home'),
	path('page/<int:article_id>/' , views.page , name = 'page'),
	path('index/' , views.index, name = 'index'),
]