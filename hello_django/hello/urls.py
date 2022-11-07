from django.urls import URLPattern, path
from hello import views

urlpatterns = [
    path("services/", views.services, name="services"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("", views.home, name="home")
]