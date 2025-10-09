from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    """
    This is a form for Post Model
    """

    class Meta:
        model = Post
        fields = ["title", "content", "status", "category", "published_date"]
