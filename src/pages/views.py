from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def worker_view(request, *args, **kwargs):
    return render(request, "panel_home.html", {})