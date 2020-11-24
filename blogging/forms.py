from django.forms import ModelForm
from blogging.models import Post


class MyCommentForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']



# Creating a form to add a post.
# form = MyCommentForm()


# Creating a form to change an existing post.
# post = Post.objects.get(pk=1)
# form = MyCommentForm(instance=post)