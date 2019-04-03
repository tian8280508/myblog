from django.shortcuts import render
from django.template import loader
from django.http import Http404
from .models import Article,User

# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse("index test~")

def page(request , article_id):
	try:
		article = Article.objects.get(articleid = article_id);
		context = {
			'article' : article
		}
	except Article.DoesNotExist:
		raise Http404("Article Does not Exist")
	return render(request, 'blog/page.html' , context);
	


def home(request):
	context = {
		'test' : '1234'
	}
	return render(request, 'blog/index.html',context)