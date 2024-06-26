from django import forms
from tinymce.widgets import TinyMCE
from .models import Post, Comment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post

        fields = ('title', 'overview', 'content', 'thumbnail',
                  'categories', 'previous_post', 'next_post', 'author')


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Your Comment',
        'id': 'comment',
        'rows': '6',
    }))

    class Meta:
        model = Comment
        fields = ('content',)
