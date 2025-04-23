from typing import Any

from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from app.models import Article
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

#LoginRequireMixin verifies user must be logged in, in order to see, create
#and delete articles. get_queryset function allows the users to view articles, that they created
class ArticleListView(LoginRequiredMixin,ListView):
    template_name = "app/home.html"
    model = Article
    context_object_name = "articles"

    def get_queryset(self) -> QuerySet[Any]:
        return Article.objects.filter(creator=self.request.user).order_by("-created_at")


class ArticleCreateView(LoginRequiredMixin,CreateView):
    template_name = "app/article_create.html"
    model = Article
    fields = ["title","status","content","twitter_post"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    

#UserPassesTextMixin, overrides test in order to access this page 
class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    template_name = "app/article_update.html"
    model = Article
    fields = ["title","status","content","twitter_post"]
    success_url = reverse_lazy("home")
    context_object_name = "articles"

    #verfies that logged in user, is the creator of the object
    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().creator


class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    template_name = "app/article_delete.html"
    model = Article
    success_url = reverse_lazy("home")
    context_object_name = "articles"

    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().creator





