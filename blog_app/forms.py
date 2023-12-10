from django import forms
from django.forms import Textarea
from .models import BlogPost, Blog, Category
from users.models import CustomUser



# from django import forms
# from .models import BlogPost

# class AddNewPostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ['blog', 'title', 'description', 'body', 'author', 'image']


class AddNewPostForm(forms.ModelForm):
    title = forms.CharField(required=True,
                            label="",
                            max_length='100',
                            widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    description = forms.CharField(required=True, label="", max_length=250,
                                  widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}))
    body = forms.CharField(required=True, label="", widget=forms.widgets.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}))
    author = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.all(), widget=forms.CheckboxSelectMultiple)
    image = forms.ImageField(required=False, max_length=None, allow_empty_file=True)

    class Meta:
        model = BlogPost
        fields = ['blog','title', 'description', 'body', 'author', 'image']
