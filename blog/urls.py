from django.urls import path
from .views import createPaper, getPaper, home, Papers, deletePaper

urlpatterns = [
    path("", home, name="blog-home" ),
    path("papers/", Papers, name="blog-papers"),
    path("create/", createPaper, name="blog-create"),
    path("paper/<id>/delete", deletePaper, name="blog-paper-delete"),
    path("paper/<id>/", getPaper, name="blog-paper"),

]