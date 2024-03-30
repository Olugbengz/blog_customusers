from django import forms
from django.forms import Textarea
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_ckeditor_5.widgets import CKEditor5Widget
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
    body = forms.CharField(required=True, label="", widget=CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"))
    author = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.all(), widget=forms.CheckboxSelectMultiple)
    image = forms.ImageField(required=False, max_length=None, allow_empty_file=True)

    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["body"].required = False

    class Meta:
        model = BlogPost
        fields = ['blog','title', 'description', 'body', 'author', 'image']
        # widgets = {
        #       "body": CKEditor5Widget(
        #           attrs={"class": "django_ckeditor_5"}, config_name="body"
        #       )
        #   }


class LoginForm(forms.ModelForm):
    pass

