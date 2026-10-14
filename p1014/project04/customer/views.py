from django.shortcuts import render

# Create your views here.
def notice(request):
    return render(request, 'notice.html')
def notice_view(request):
    return render(request, 'notice_view.html')
def inquiry(request):
    return render(request, 'inquiry.html')
def guide(request):
    return render(request, 'guide.html')
def faq(request):
    return render(request, 'faq.html')