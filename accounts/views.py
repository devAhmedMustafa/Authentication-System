from django.shortcuts import render
from .forms import NewUser
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import CustomUser as User


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer = UserSerializer


def sign_up(request):
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)

            return HttpResponse('Done')
        
    form = NewUser()

    return render(request, 'sign_up.html', {'form': form})


def login(request):
    if request.method == 'post':

        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            auth_login(request, user)
            return JsonResponse(user)

    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return JsonResponse({'message':'logged out'})