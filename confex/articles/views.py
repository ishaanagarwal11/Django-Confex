from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.core.mail import send_mail
from django.conf import settings

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug): 
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article}) 

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)  
            instance.author = request.user
            instance.save()
            
            email = request.POST.get('email')
            title = request.POST.get('title')
            uploader = request.POST.get('author')

            #send email
            send_mail(
                'New Paper Uploaded',
                title,
                'email',[email], fail_silently=False)

            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})


@login_required(login_url="/accounts/login/")
def my_articles(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)  
            instance.author = request.user
            instance.save()
            return redirect('articles:my_articles')
    else:
        form = forms.CreateArticle()
    
    articles = Article.objects.filter(author=request.user).order_by('date')
    return render(request, 'articles/my_articles.html', {'form': form, 'articles': articles})


@login_required(login_url="/accounts/login/")
def delete_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:my_articles')
    return HttpResponseNotAllowed(['POST'])
