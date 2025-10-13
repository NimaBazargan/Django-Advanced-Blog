from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "blog"

urlpatterns = [
    # path('cbv-index/',TemplateView.as_view(template_name='index.html',extra_context={"name":"ali"})),
    path("cbv-index/", views.IndexView.as_view(), name="index"),
    # path('go-to-index',RedirectView.as_view(pattern_name='blog:index'),name='redirect-to-index'),
    path(
        "go-to-maktab/<int:pk>/",
        views.RedirectToMaktab.as_view(),
        name="redirect-to-maktab",
    ),
    path("post/", views.PostListView.as_view(), name="post-list"),
    path("post/api/", views.PostListApiView.as_view(), name="post-list-api"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit/", views.PostEditView.as_view(), name="post-edit"),
    path("post/<int:pk>/delete", views.PostDeleteView.as_view(), name="post-delete"),
    path("api/v1/", include("blog.api.v1.urls")),
]
