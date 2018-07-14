from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signin/', signin, name='login'),
    path('signup/', signup, name="signup"),
    path('signout/', signout, name='signout'),

    path('edit/', edit_profil, name='edit_profil'),
    path('profil/', view_profil, name='view_profil'),
]