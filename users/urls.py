from django.urls import path

from .views import sign_up, login, logout


urlpatterns = [
    path('sign-up/', sign_up),
    path('login/', login),
    path('logout/', logout),
]