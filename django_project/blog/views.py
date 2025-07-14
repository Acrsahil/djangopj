from django.http import HttpResponse
from .models import Post
from django.shortcuts import render


def home(request):
    supllex = {'posts': Post.objects.all()}
    return render(request, "blog/home.html", supllex)



def about(request):
    return render(request, "blog/about.html", {"title": "About Us"})


# /contactus/ URL will call this view


def contactus(request):
    return HttpResponse("<H1>Blog contactus</H1>")


# /add/<int:a>/<int:b> URL will call this view


def add(request, a, b):
    result = int(a) + int(b)
    return HttpResponse(f"<h1>sum of {a} and {b} is {result}</h1>")
