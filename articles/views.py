from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DeleteView,
    UpdateView,
    DetailView,
    CreateView,
    )
from .models import Article
# Create your views here.


class ArticleListView(ListView):
    template_name = 'article_list.html'
    model = Article
    login_url = 'login'

class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    model = Article
    login_url = 'login'
        
class ArticleUpdateView(UpdateView):
    template_name = 'article_edit.html'
    model = Article
    fields = ('title', 'body',)
    login_url = 'login'

class ArticleDeleteView(DeleteView):
    template_name = 'article_delete.html'
    model = Article
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    
class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'article_new.html'
    model = Article
    fields = ('title', 'body',)
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)