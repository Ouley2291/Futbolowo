from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Video
from .forms import VideoForm

ALLOWED_ROLES = ['trener', 'wlasciciel', 'admin']

@login_required
def upload_highlight(request):
    if not request.user.is_staff:
        if not hasattr(request.user, 'profile') or request.user.profile.role not in ALLOWED_ROLES:
            return redirect('matches:highlights_list')

    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.uploaded_by = request.user
            video.save()
            return redirect('matches:highlights_list')
    else:
        form = VideoForm()

    return render(request, "matches/upload_highlight.html", {
        "form": form
    })


def highlights_list(request):
    highlights = Video.objects.all().order_by('-created_at')
    return render(request, "matches/highlights.html", {
        "highlights": highlights
    })