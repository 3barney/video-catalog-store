from django.shortcuts import render

# Create your views here.
def index(request):
  # #rd param object that contains data to be displayed in the template.
  return render(request, 'main/index.html', {})
