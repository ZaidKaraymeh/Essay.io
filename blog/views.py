from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Essay
from django.contrib import messages

from .forms import EssayForm
import ast
# Create your views here.

def home(request):

    

    return render(request, "blog/home.html", {})
@login_required
def Papers(request):

    author = request.user
    papersNonCleaned = Essay.objects.filter(author=author)

    # reverses list
    papers = [{"title": x[2], "content": x[3], "id": x[0]} for x in papersNonCleaned.values_list()]

    papers = list(reversed(papers))

    

    context = {"papers": papers  }
    return render(request, "blog/papers.html", context)

@login_required
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
@login_required
def deletePaper(request, id):
    paper = Essay.objects.filter(id=id)
    paper.delete()
    messages.info(request, "Essay Deleted!")
    return redirect("blog-papers")

@login_required
def getPaper(request, id):

    papersNonCleaned = Essay.objects.filter(id=id)
    paper = [{"title": x[2], "content": x[3], "id": x[0]} for x in papersNonCleaned.values_list()]
    context = {"paper": paper[0]}
    return render(request, "blog/paper.html", context)
    
@login_required
def editPaper(request, id):
    obj = Essay.objects.filter(id=id).first()
    if request.method == "POST":
        form = EssayForm(request.POST or None, instance=obj)

        if form.is_valid():
            form.save(commit=False)
            form.save()
            messages.success(request, "Essay Edited!")
            return redirect("blog-paper", id=obj.id)
    else:
        form = EssayForm(instance=obj)

    context = {"form": form, "id":id}

    return render(request, "blog/edit.html", context)