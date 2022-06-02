from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .models import *


# Create your views here.


@login_required(login_url='/accounts/login/')
def homepage(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def profile(request,user_id):
    current_user=get_object_or_404(User,id=user_id)
    # current_user = request.user
    profile = get_object_or_404(Profile,id = current_user.id)
    return render(request, 'profile/profile.html', { "profile": profile})

