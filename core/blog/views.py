from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class IndexView(TemplateView):
    """
    a class base view to show index page
    """
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'nima'
        return context
    
class RedirectToMaktab(RedirectView):
    """
    a class redirect view to redirect to maktabkhooneh
    """
    url= "https://maktabkhooneh.com"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post,id=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    
class PostListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    """
    a class list view to show posts
    """
    permission_required = 'blog.view_post'
    # model = Post
    queryset = Post.objects.filter(status=True)
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts
    paginate_by = 2
    ordering = '-id'
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin,DetailView):
    """
    a class detail view to show detail of desired post
    """
    model = Post
    # template_name = "blog/post_detail.html"

# class PostCreateView(FormView):
#     template_name = 'blog/contact.html'
#     form_class = PostForm
#     success_url = '/blog/post'
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.save()
#         return super(PostCreateView, self).form_valid(form)(

class PostCreateView(LoginRequiredMixin,CreateView):
    """
    A class create view to create a new post
    """
    model = Post
    # fields = ['author','title','content','status','category','published_date']
    form_class = PostForm
    success_url = '/blog/post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostEditView(LoginRequiredMixin,UpdateView):
    """
    a class update view to edit desire post
    """
    model = Post
    form_class= PostForm
    success_url = '/blog/post'

class PostDeleteView(LoginRequiredMixin,DeleteView):
    """
    a class delete view to delete a post
    """
    model = Post
    success_url = '/blog/post'