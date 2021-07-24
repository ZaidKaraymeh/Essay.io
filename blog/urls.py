from django.urls import path
from .views import about, createPaper, editPaper, getPaper, home, Papers, deletePaper

urlpatterns = [
    path("", home, name="blog-home" ),
    path("papers/", Papers, name="blog-papers"),
    path("about/", about, name="blog-about"),
    path("create/", createPaper, name="blog-create"),
    path("paper/<int:id>/delete", deletePaper, name="blog-paper-delete"),
    path("paper/<int:id>/", getPaper, name="blog-paper"),
    path("paper/<int:id>/edit", editPaper, name="blog-paper-edit"),

]