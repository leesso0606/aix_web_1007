from django.shortcuts import render
import os
from pathlib import Path
from dotenv import load_dotenv

# Create your views here.
def step01(request):
    # 디펙토리 위치 :부모의 부모로 가서
    BASE_DIR =Path(__file__).resolve().parent.parent
    ENV_FILE =BASE_DIR /'.env'
    load_dotenv(ENV_FILE)
    naver_key=os.getenv('naver_key')
    return render(request, 'step01.html')