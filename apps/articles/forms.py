from django import forms
from .models import Comment, Article
from django_ckeditor_5.widgets import CKEditor5Widget

class CreateArtcileForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget())

    class Meta:
        model = Article
        fields = ('title','category','content','thumbnail',)


class EditArticleForm(CreateArtcileForm):
    class Meta(CreateArtcileForm.Meta):
        fields =  ('title','category','content',)


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