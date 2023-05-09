from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserList)

urlpatterns = [
    path('api/users', include(router.urls)),
    path('register/', views.sign_up, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
