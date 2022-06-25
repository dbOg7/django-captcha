from django.shortcuts import render, HttpResponse
from .forms import CaptchaTestForm

# Create your views here.

def home(request):
    if request.method == "POST":
        form=CaptchaTestForm(request.POST)
        if form.is_valid():
            return HttpResponse('success')
        else:
            return HttpResponse('failed')

    form=CaptchaTestForm()
    
    return render(request,"home.html",{"form":form })