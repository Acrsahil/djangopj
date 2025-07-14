from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about"),
    path("contactus/", views.contactus, name="blog-contactus"),
    path("add/<int:a>/<int:b>", views.add, name="blog-add"),
]
