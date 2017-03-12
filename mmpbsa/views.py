from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import *

import sys

TEMPLATE_PATH = '/home/liangzhen/webserver/mulab/mmpbsa/templates/'  # use your own username here
if TEMPLATE_PATH not in sys.path:
    sys.path.append(TEMPLATE_PATH)

def index(request):
    #request.POST.ff
    if request.method == "POST" :
        form = ParametersForm(request.POST, request.FILE,
        initial={'pdie':'4.0','saltconc':"0.15", 'ligand':"SUB"}
        )
        if form.is_valid() :
            newdoc = form.FileField['docfile']
            print("Upload File "+newdoc)
            dataset = form.cleaned_data
            dataset['url'] = "http://127.0.0.1:8001/mmpbsa/results/"
            #return render(request, 'parameters.html',{'pdie':pdie, 'saltconc':saltconc, "ligand":ligand})
            return render(request, 'parameters.html', dataset)
    else :
        form = ParametersForm()

    return render(request, "index.html",{'form':form})
    #return HttpResponse("Hello, world. You're at the polls index.")

def theory(request):
    #text="<h2>A hello massage</h2>"
    #return HttpResponse(text)
    #return redirect("http://www.google.com")
    #return redirect(result, mmpbsa=175.1, std=8.97)
    return render(request, "theory.html",{})

def result(request):

    return render(request, "result.html", {})

def login(request):
    username = "not logged in"

    if request.method == "POST":
        print("HAHAHHA")
        #Get the posted form
        MyLoginForm = LoginForm(request.POST)
        print(MyLoginForm.is_valid())

        if MyLoginForm.is_valid():
            print(MyLoginForm.cleaned_data)
            username = MyLoginForm.cleaned_data['user']
            print(username)
            return render(request, 'loggedin.html', {"username" : username})
        else :
            print("ADADADA")
            #return render(request, 'login.html', {})
            return HttpResponseRedirect('/mmpbsa/login/')
    else:
        MyLoginForm = LoginForm()
        return render(request, 'login.html', {})
        #return HttpResponseRedirect('/mmpbsa/login/')

        #return render(request, 'loggedin.html', {"username" : username})

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
            name = form.cleaned_data['your_name']
            print("Login For User Name "+name)
            return render(request, 'welcome.html', {"your_name": name })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def upload(request):
    return render(request, 'upload.html', {})
