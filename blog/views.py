from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Essay
from django.contrib import messages

from .forms import EssayForm
import ast
# Create your views here.

def home(request):

    

    return render(request, "blog/home.html", {})

def Papers(request):

    author = request.user
    papersNonCleaned = Essay.objects.filter(author=author)

    # reverses list
    papers = [{"title": x[2], "content": x[3], "id": x[0]} for x in papersNonCleaned.values_list()]

    papers = list(reversed(papers))

    

    context = {"papers": papers  }
    return render(request, "blog/papers.html", context)

def getPaper(request, id):

    papersNonCleaned = Essay.objects.filter(id=id)
    paper = [{"title": x[2], "content": x[3], "id": x[0]} for x in papersNonCleaned.values_list()]
    print(paper)
    context = {"paper": paper[0]}
    return render(request, "blog/paper.html", context)


def createPaper(request):
    if request.method == "POST":
        form = EssayForm(request.POST)

        if form.is_valid():
            essay = form.save(commit=False)
            essay.author = request.user
            form.save()
            messages.success(request, "Essay Posted!")
            return redirect("blog-papers")
    else:
        form = EssayForm()
    

    context = {"form": form}
    return render(request, "blog/create.html", context)

def deletePaper(request, id):
    paper = Essay.objects.filter(id=id)
    paper.delete()
    messages.info(request, "Essay Deleted!")
    return redirect("blog-papers")