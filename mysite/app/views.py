from django.shortcuts import render, HttpResponseRedirect
from .forms import CaptchaTestForm

# Create your views here.
def home(request):
    if request.method=="POST":
        form=CaptchaTestForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('yeaaaaaahhhh')
        else:
            print("fail")
    form=CaptchaTestForm()
    return render(request,"home.html",{"form":form})