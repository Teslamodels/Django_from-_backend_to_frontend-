from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render
from random import randint

def Blog(request):
    number = randint(1, 50)
    return render(request, "index.html", context={'time': timezone.now(), 'Numbers': number})