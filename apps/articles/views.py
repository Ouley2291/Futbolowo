from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import CommentForm, CreateArtcileForm, EditArticleForm


@login_required
def add(request):
    if not request.user.is_staff:
        return redirect('core:index')
    
    if request.method == 'POST':
        form = CreateArtcileForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(commit=False)
            article.creator = request.user
            article.save()
            return redirect('articles:list')

    else:
        form = CreateArtcileForm()

    return render(request, "articles/create_article.html", {
        "form": form,
    })

@login_required
def edit(request, id):
    if not request.user.is_staff:
        return redirect('articles:view', pk=id)
    
    article = get_object_or_404(Article, pk=id)
    
    if request.method == 'POST':
        form = EditArticleForm(request.POST, request.FILES, instance=article)

        if form.is_valid():
            form.save()
            return redirect('articles:view', id=article.id)

    else:
        form = EditArticleForm(instance=article)

    return render(request, "articles/edit_article.html", {
        "form": form,
    })


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