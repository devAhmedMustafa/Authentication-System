from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from .forms import NewUser
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.http import HttpResponse, JsonResponse
from .functions import send_email_verify
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, authentication, status
from .serializers import UserSerializer
from .models import CustomUser as User
from .token import account_activation_token


def activate(request, pk, token):

    try:
        user = User.objects.get(pk=pk)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        auth_login(request, user)

    return HttpResponse('account activated')


class UserList(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


# NORMAL DJANGO
def sign_up(request):
    if request.method == 'POST':
        domain = get_current_site(request).domain

        form = NewUser(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False
            user.save()

            send_email_verify(user, domain)

            return HttpResponse('Done')
        
    form = NewUser()

    return render(request, 'sign_up.html', {'form': form})


def login(request):
    if request.method == 'POST':

        domain = get_current_site(request).domain
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.get(email__exact=email)

        if user.is_active:

            user = authenticate(email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponse('you\'r logged in')

            else:
                return HttpResponse('Invalid email or password')

        else:
            send_email_verify(user, domain)
            return HttpResponse('Your account is not activated, we sent you email verifying')

    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return JsonResponse({'message':'logged out'})