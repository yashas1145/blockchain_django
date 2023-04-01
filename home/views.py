from django.shortcuts import render

from home.models import Block

# Create your views here.

def home(request):
    return render(request, 'home/home.html', {})

def add_block(request):
    
    if request.method == 'POST':

        dataWord = request.POST.get('dataword')

        if Block.objects.count() == 0:

            BlockObject = Block(data=dataWord, hash=abs(hash('1' + dataWord)), prev_hash='-1')

        else:
            
            tempBlock = Block.objects.all()
            blockId = [i.id for i in list(tempBlock)][-1]
            previous = [i.hash for i in list(tempBlock)][-1]
            BlockObject = Block(data=dataWord, hash=abs(hash(str(blockId) + dataWord)), prev_hash=previous)
        
        BlockObject.save()

        return render(request, 'home/home.html', {})