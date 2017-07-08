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
    return render(request, 'index.html', NAV)
    
# def all_news(request, word_id):
#     card = Card.objects.filter(id=word_id).first() 
#     if not card:
#         return HttpResponseNotFound('No such card')
def all_news(request):
    return render(request,'new_card.html', dict(title="Создание новой карточки", 
        nav_link_1="/cards/", nav_link_2="/training/", 
        nav_link_1_name="Все карточки", nav_link_2_name="Тренировка"))

def all_cards(request):
    return render(request,'all_cards.html', dict(title="Все карточки", 
        nav_link_1="/new/", nav_link_2="/training/", 
        nav_link_1_name="Создание новой карточки", nav_link_2_name="Тренировка",
        cards = [1, 2, 3, 4, 5, 6, 7, {'name': 'HELLO'}]))

def training(request):
    return render(request,'training.html', dict(title="Тренировка", 
        nav_link_1="/new/", nav_link_2="/cards/", 
        nav_link_1_name="Создание новой карточки", nav_link_2_name="Все карточки"))

def results(request, word_id):
    response = "You're looking at the meaning of word %s."
    return HttpResponse(response % word_id)
# Create your views here.