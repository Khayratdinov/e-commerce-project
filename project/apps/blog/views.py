from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# ============================================================================ #
from project.apps.common.models import HeadImages
from project.apps.blog.models import Blog, CategoryBlog, BlogComment
from project.apps.blog.forms import BlogCommentForm
from project.apps.core.utils import paginate_queryset

# Create your views here.


# =================================== BLOG =================================== #


def blog_list(request):
    blog_list = Blog.objects.filter(status="True").order_by("-created_at")

    blog_list = paginate_queryset(request, blog_list)

    context = {
        "blog_list": blog_list,
    }
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, slug):
    blog_detail = get_object_or_404(Blog, slug=slug)
    blog_detail.views += 1
    blog_detail.save()
    blog_comment = BlogComment.objects.filter(blog=blog_detail)
    context = {
        "blog_detail": blog_detail,
        "blog_comment": blog_comment,
    }
    return render(request, "blog/blog_detail.html", context)


# =============================== CATEGORY BLOG ============================== #


def category_blog_detail(request, slug):
    blog_category = get_object_or_404(CategoryBlog, slug=slug)
    blog_list = Blog.objects.filter(category=blog_category, status="True").order_by(
        "-created_at"
    )

    blog_list = paginate_queryset(request, blog_list)
    context = {
        "blog_category": blog_category,
        "blog_list": blog_list,
    }
    return render(request, "blog/blog_list_by_category.html", context)


# ================================== COMMENT ================================= #


def add_comment_to_blog(request, blog_id):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            data = BlogComment()
            data.blog_id = blog_id
            data.name = form.cleaned_data["name"]
            data.email = form.cleaned_data["email"]
            data.phone = form.cleaned_data["phone"]
            data.comment = form.cleaned_data["comment"]
            data.ip = request.META.get("REMOTE_ADDR")
            data.save()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)