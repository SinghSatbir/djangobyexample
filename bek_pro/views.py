from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from bek_pro.models import Item


def index(request):
        template=loader.get_template('index.html')
        context={
            'variable1':Item.objects.get(id=1),
            #variable to store items
        }
        return HttpResponse(template.render(context,request))