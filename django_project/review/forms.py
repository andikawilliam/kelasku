from django.forms import ModelForm, Textarea
from review.models import Post

class ReviewForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'rating', 'content']
        widgets = {
            'content': Textarea(attrs={'cols': 40, 'rows': 15})
        }