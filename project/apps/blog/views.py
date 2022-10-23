from django.shortcuts import render, get_object_or_404

# ============================================================================ #
from project.apps.common.models import HeadImages
from project.apps.blog.models import Blog

# Create your views here.


# =================================== BLOG =================================== #


def blog_list(request):
    blog_list = Blog.objects.filter(status="True").order_by("-create_at")
    bradcaump_img = HeadImages.objects.filter(status=True).order_by("?")[:1]

    context = {
        "blog_list": blog_list,
        "bradcaump_img": bradcaump_img,
    }
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, slug):
    bradcaump_img = HeadImages.objects.filter(status=True).order_by("?")[:1]
    blog_detail = get_object_or_404(Blog, slug=slug)
    blog_detail.views += 1
    blog_detail.save()
    context = {
        "blog_detail": blog_detail,
        "bradcaump_img": bradcaump_img,
    }
    return render(request, "blog/blog_detail.html", context)
