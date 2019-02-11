from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
	return HttpResponse("母亲大人新年快乐~")

def articlePage(request , article_id):
	title = Article.objects();
	return HttpResponse(output);

def index(request):
	return HttpResponse('index page')