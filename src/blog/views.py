from django.shortcuts import render

# Create your views here.
from .models import blog_post


def blog_post_detail_page(request):
    obj = blog_post.objects.get(id=1)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)