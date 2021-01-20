from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.


def homepage_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about me",
        "my_number": 123,
        "val": [1, 2, 3]
    }
    return render(request, "about.html", my_context)
