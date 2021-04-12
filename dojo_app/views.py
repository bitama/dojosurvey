from django.shortcuts import render,redirect,HttpResponse


def index(request):
    return render( request,"index.html")

def display_user(request):
    name_from_form = request.POST["name"]
    location_from_form = request.POST["location"]
    language_from_form = request.POST["language"]
    comment_from_form = request.POST["comment"]
    context = {
        "name":name_from_form,
        "location":location_from_form,
        "language":language_from_form,
        "comment":comment_from_form    
    }
    return render( request,"display.html",context)
    

