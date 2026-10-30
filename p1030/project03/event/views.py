from django.shortcuts import render

# Create your views here.
def event(request):
    return render(request, 'event.html')

def eview(request):
    return render(request, 'eview.html')