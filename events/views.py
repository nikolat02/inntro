# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from events.admin import EventAdmin
from .models import Event

# Create your views here.

def Hello_World(requests):
    # template = loader.get_template('admin/events/change_list.html')
    # context = {
    #     'previous_month':previous_month,
    #     'next_month': next_month,
    # }
    # return HttpResponse(template.render(context,requests))
    return HttpResponse('Hello World')