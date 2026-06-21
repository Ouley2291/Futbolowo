from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Profile
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('core:index')
    else:
        form = RegisterForm()

    print(form)
    return render(request, 'accounts/register.html', {
        "form": form,
    })
