from django.urls import path
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from . import views
from .forms import AuthenticationForm

urlpatterns = [
  path(r'', views.index, name='index'), # First param '', url to match, 2nd is func to be executed, 3rd name sets url name
  path(r'accounts/login', login, {
    'template_name': './login.html',
    'authentication_form': AuthenticationForm
  }, name='login'),
  path(r'accounts/logout', logout, {
    'next_page': '/'
  },  name='logout'),
]