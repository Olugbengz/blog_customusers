from django import forms
from django.forms import Textarea
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from djrichtextfield.widgets import RichTextWidget
from .models import BlogPost, Comment, Blog, Category
from users.models import CustomUser





class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

        widgets = {
            'comment_text': forms.Textarea(attrs={'rows':3, 'cols':50, 'placeholder': 'Add comment ...'})
        }
        labels = {
            'comment_text': ''
        }


class AddNewPostForm(forms.ModelForm):
    title = forms.CharField(required=True,
                            label="",
                            max_length='100',
                            widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    description = forms.CharField(required=True, label="", max_length=250,
                                  widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}))
    body = forms.CharField(required=True, label="", widget=RichTextWidget())
    author = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.all(), widget=forms.CheckboxSelectMultiple)
    image = forms.ImageField()

    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["body"].required = False

    class Meta:
        model = BlogPost
        fields = ['blog','title', 'description', 'body', 'author', 'image']
        


