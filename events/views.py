# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.template import loader
from events.admin import EventAdmin
from django.contrib.auth.models import User
from .models import Event
from .forms import SignUpForm

# Create your views here.

# def Hello_World(requests):
#     template = loader.get_template('admin/events/change_list.html')
#     context = {
#         'previous_month':previous_month,
#         'next_month': next_month,
#     }
#     return HttpResponse(template.render(context,requests))

def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = SignUpForm()
        return render(request,'events/signup.html',{'form':form})
    
  