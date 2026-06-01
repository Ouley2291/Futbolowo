from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import CommentForm


@login_required
def add(request):
    pass


def article_view(request, id):
    article = get_object_or_404(Article, pk=id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()

        return redirect('articles:view', id)
    else:
        comment_form = CommentForm()

    comments = article.comments.all()

    return render(request, "articles/article_view.html", {
        "article": article,
        "form": comment_form,
        'comments': comments,
    })


def article_list(request):
    articles = Article.objects.all().order_by("-created_at")
    if 'category' in request.GET:
        category = request.GET['category']
    else:
        category = ''

    if category:
        articles = articles.filter(category=category)

    return render(request, "articles/article_list.html", {
        "articles": articles,

    })