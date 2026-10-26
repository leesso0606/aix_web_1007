from django.shortcuts import render
from customer.models import Board

# Create your views here.

def cview(request,bno):
    qs=Board.objects.filter(bno=bno)[0]
    print('확인:',qs)
    context={'board':qs}
    return render(request, 'cview.html', context)



def clist(request):
    qs=Board.objects.all().order_by('-bgroup','bhit')
    context={'list':qs}
    return render(request, 'clist.html',context)