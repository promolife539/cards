from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound 
from .models import Card

NAV = {'nav': [
        {'name': 'Главная страница',
         'link': '/main'},
        {'name': 'Новые слова',
         'link': '/not-main'},
         {'name': 'результаты', 'link': '/results'}
    ]}

def index(request):
    return render(request, 'main/index.html', NAV)
    
def new_word(request, word_id):
    card = Card.objects.filter(id=word_id).first() 
    if not card:
        return HttpResponseNotFound('No such card')
    

def results(request, word_id):
    response = "You're looking at the meaning of word %s."
    return HttpResponse(response % word_id)
# Create your views here.