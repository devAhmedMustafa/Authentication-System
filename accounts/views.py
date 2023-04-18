from django.shortcuts import render
from .forms import NewUser
from django.contrib.auth import login as auth_login, authenticate
from django.http import HttpResponse

# Create your views here.

def sign_up(request):

    if request.method == 'POST':

        form = NewUser(request.POST)
        
        if form.is_valid():

            user = form.save()
            auth_login(user, request)

            return HttpResponse(f'Hello${request.user}')

    return render(request, 'sign_up.html')