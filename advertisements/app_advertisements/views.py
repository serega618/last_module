from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Успешна! Вы на главной')

def page1(request):
    return HttpResponse('Успешно это другая') 