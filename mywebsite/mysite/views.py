from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# Create your views here.
def registerpage(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"register.html",context={'form':form})

def loginpage(request):
    return render(request,"login.html",)