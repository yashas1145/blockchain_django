from django.shortcuts import render

from home.models import Block

# Create your views here.

def view(request):
    return render(request, 'view/view.html', {'blocks':Block.objects.all(), 'count':Block.objects.count()})