from django import forms
from .models import Comment, Article

class CreateArtcileForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','category','content','thumbnail',)

        widgets = {
            'title': forms.Textarea(attrs={
                "placeholder": "Tytul artykulu",
                "class": "w-full px-6 py-4 rounded-xl border focus:ring-2 focus:ring-indigo-500"
            })
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        widgets = {
            'content': forms.Textarea(attrs={
                "placeholder": "Pozostaw komentarz....",
                "rows": 3,
                "class": "w-full px-6 py-4 rounded-xl border focus:ring-2 focus:ring-indigo-500"
            })
        }