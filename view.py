# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect,JsonResponse


def login(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    nextpath = request.GET.get('next','')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        if nextpath is not None:
            return HttpResponseRedirect(nextpath)
        else:
            return HttpResponseRedirect("/assets/")
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/accounts/login/")

def logprofile(request):
    return HttpResponseRedirect("/assets/")


