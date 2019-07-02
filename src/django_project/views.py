from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    title = "Homepage Title"
    context = {"title": "random_title"}
    if request.user.is_authenticated:
            context = {"title": title, "my_list": [1, 2, 3, 4, 5]}
    return render(request, "home.html", context)

def about_page(request):
    title = "About Title"
    return render(request, "about.html", {"title": title})

def contact_page(request):
    title = "Contact Title"
    return render(request, "helloworld.html", {"title": title})

def example_page(request):
    context = {"title": "Example"}
    template_name = "helloworld.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))

