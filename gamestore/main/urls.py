from django.urls import path
from . import views

urlpatterns = [
  path(r'', views.index, name='index'), # First param '', url to match, 2nd is func to be executed, 3rd name sets url name
]