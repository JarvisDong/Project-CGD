from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("我敲里吗！！")

# Create your views here.
