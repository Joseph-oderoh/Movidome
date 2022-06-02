from django.shortcuts import  render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Image
from .forms import *
from .models import*



# Create your views here.


@login_required(login_url='/accounts/login/')
def homepage(request):
    profiles=   Profile.objects.all()
    return render(request, 'index.html', {'profiles': profiles})


@login_required(login_url='/accounts/login/')
def profile(request,profileId):

    profile = Profile.objects.get(pk = profileId)
    images = Image.objects.filter(id=profile.id).all()

    return render(request,"profile/profile.html",{"profile":profile,"images":images})



@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('homepage')

    else:
        form = NewProfileForm()
    return render(request, 'profile/update_profile.html', {"form": form})


