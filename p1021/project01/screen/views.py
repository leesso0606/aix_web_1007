from django.shortcuts import render
from screen.models import Screen
from django.db.models import F,Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def map(request):
    return render(request, 'map.html')







# ---------------------------------------------------------------------------

# 차트그래프
def chart(request):
    # qs = Screen.objects.filter(title__contains='가')
    # qs = Screen.objects.filter(crevenue__gte=1160000000)
    # qs = Screen.objects.filter(Q(crevenue__gte=1160000000)|Q(title__contains='가'))
    # print("검색 : ",qs)
    # for s in qs:
    #     print(f'{s.title},{s.crevenue:,}')
    # print("검색개수 : ",qs.count())

    return render(request,'s_chart.html')



# ajax통신
def chart_data(request):
    search_word= request.POST.get('search_word','')
    qs = Screen.objects.filter(Q(crevenue__gte=1160000000)|Q(title__contains='가')).values()[:6]
    r_qs = list(qs)
    context = {'list':r_qs}
    return JsonResponse(context)