from django.shortcuts import render
from django.http import HttpResponse
#views
def first(request):
    return HttpResponse("first")
