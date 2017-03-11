from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from .forms import *

def index(request):
    #request.POST.ff
    return render(request, "/home/liangzhen/webserver/mulab/mmpbsa/templates/index.html",{})
    #return HttpResponse("Hello, world. You're at the polls index.")

def theory(request):
    #text="<h2>A hello massage</h2>"
    #return HttpResponse(text)
    #return redirect("http://www.google.com")
    #return redirect(result, mmpbsa=175.1, std=8.97)
    return render(request, "/home/liangzhen/webserver/mulab/mmpbsa/templates/theory.html",{})

def result(request):

    return render(request, "/home/liangzhen/webserver/mulab/mmpbsa/templates/result.html", {})


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect( '/home/liangzhen/webserver/mulab/mmpbsa/templates/welcome.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, '/home/liangzhen/webserver/mulab/mmpbsa/templates/name.html', {'form': form})
