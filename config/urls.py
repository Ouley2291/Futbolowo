"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from apps.accounts.forms import LoginForm
from apps.accounts import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('register/', v.register, name="register"),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm, template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts', include('apps.accounts.urls')),
#    path('contact', include('apps.contact.urls')),
#    path('gallery', include('apps.gallery.urls')),
#    path('matches', include('apps.matches.urls')),
#    path('articles', include('apps.articles.urls')),
    path('players', include('apps.players.urls')),
#    path('teams', include('apps.teams.urls')),
]
