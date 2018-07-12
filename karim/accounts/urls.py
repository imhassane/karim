from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signin/', signin, name='login'),
    path('signup/', signup, name="signup"),
    path('signout/', signout, name='signout'),
]