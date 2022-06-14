from django.shortcuts import render
from .forms import CaptchaTestForm

# Create your views here.

def home(request):
    if request.method == "POST":
        form=CaptchaTestForm(request.POST)
        if form.is_valid():
            return render(request, "success.html")
    form=CaptchaTestForm()
    return render(request,"home.html",{"form":form })