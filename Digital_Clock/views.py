from django.shortcuts import render
from django.utils import timezone

# Create your views here.
def index(request):
    time = timezone.localtime(timezone.now())
    return render(request, 'digital_clock/index.html', {
        'time' : time,
    })