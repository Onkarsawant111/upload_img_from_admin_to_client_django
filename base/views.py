from django.shortcuts import render
from .models import Picture

# Create your views here.
def home(request):
    dpic = Picture.objects.all() 
    return render(request, 'onkar.html', {'dpic': dpic})