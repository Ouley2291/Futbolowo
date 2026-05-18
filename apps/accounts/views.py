from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = RegisterForm()

    print(form)
    return render(request, 'accounts/register.html', {
        "form": form,
    })
