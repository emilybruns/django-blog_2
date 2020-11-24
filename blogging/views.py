from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from blogging.serializers import UserSerializer, PostSerializer, CategorySerializer
from blogging.models import Post, Category
from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from blogging.forms import MyCommentForm


@login_required
def add_model(request):
    if request.method == "POST":
        form = MyCommentForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.created_date = timezone.now()
            model_instance.author = User
            model_instance.modified_date = None
            model_instance.published_date = timezone.now()
            model_instance.save()
            return redirect('/')

    else:

        form = MyCommentForm()

        return render(request, "my_template.html", {'form': form})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BlogListView(ListView):
    # queryset = Post.objects.order_by("-published_date")
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/list.html"

    def stub_view(request, *args, **kwargs):
        body = "Stub View\n\n"
        if args:
            body += "Args:\n"
            body += "\n".join(["\t%s" % a for a in args])
        if kwargs:
            body += "Kwargs:\n"
            body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
        return HttpResponse(body, content_type="text/plain")


class BlogDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"
