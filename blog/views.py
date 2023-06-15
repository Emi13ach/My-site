from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post
from .forms import CommentForm


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset =  super().get_queryset()
        data = queryset[:3]
        print(type(data))
        return data    
    

# def starting_page(request):
#     sorted_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#         "posts": sorted_posts,
#         })


class BlogListView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"    
    
    # # Query filter
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=0)
    #     return data
    
# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request, "blog/all-posts.html", {
#         "all_posts": all_posts
#     })


class PostDetailView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    context_object_name = "post_details"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context


# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html", {
#         "post_details": post,
#         "post_tags": post.tags.all()
#     })
    