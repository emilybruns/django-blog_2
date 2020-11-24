from django.urls import path
from blogging.views import BlogListView, BlogDetailView, add_model

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("add/", add_model, name="add_post"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
]
