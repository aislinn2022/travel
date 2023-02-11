from django.shortcuts import render
from .models import places, team


# Create your views here.
def demo(request):
    object1=places.objects.all()
    object2=team.objects.all()
    return render(request,"index.html",{'result':object1,'result2':object2})
