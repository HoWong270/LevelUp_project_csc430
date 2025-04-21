from django.shortcuts import render
from app.models import Article
from app.forms import CreateArticleFrom

def home(request):
    articles = Article.objects.all()
    return render(request, "app/home.html", {"articles":articles})

def create_article(request):
    if request.method == "POST":
        #data is submitted
        form = CreateArticleFrom(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            new_article = Article (
                title = form_data['title'],
                status = form_data['status'],
                content = form_data['content'],
                word_count = form_data['word_count'],
                twitter_post = form_data['twitter_post']

            )
            new_article.save()
    else:
        form = CreateArticleFrom()
    return render(request, "app/article_create.html", {"form": form})
    


