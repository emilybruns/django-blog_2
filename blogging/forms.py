from django.forms import ModelForm
from blogging.models import Post
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MyCommentForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text="Required. Inform a valid email address.",
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


# Creating a form to add a post.
# form = MyCommentForm()


# Creating a form to change an existing post.
# post = Post.objects.get(pk=1)
# form = MyCommentForm(instance=post)
