from django import template
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def sito_id(request, id):
    return HttpResponse("the id is  %s." % id)

def localita(request, id):
    response = "the id has localita  %s."
    return HttpResponse(response % localita)


from .models import Sito
from django.template import loader
def recenti(request):
    latest_siti = Sito.objects.order_by('-id')[:3]
    template = loader.get_template('polls/recenti.html')
    context = {
        'latest_siti': latest_siti,
    }
    from django.shortcuts import render
    return render(request, 'polls/recenti.html', context)
    #2
    #return HttpResponse(template.render(context, request))
    #1
    #output = ', '.join([q.localita for q in latest_question_list])
    #return HttpResponse(output)

from django.shortcuts import get_object_or_404

def detail(request, id):
    sito = get_object_or_404(Sito, pk=id)
    return render(request, 'polls/detail.html', {'sito ': sito})

def get_unipd(request,id):
    pass

def get_more_info(request,id):
    pass

def mapping(request):
    siti_to_map=Sito.objects.order_by('-id')
    template = loader.get_template('polls/map.html')
    context = {
        'siti_to_map': siti_to_map,
    }
    
    return render(request, 'polls/map.html', context)

    #pass
    
