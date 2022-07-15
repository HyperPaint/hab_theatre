from django.shortcuts import render, redirect

from hab_theatre.settings import ALLOWED_HOSTS
from hab_theatre.urls import theatre

from . import paths
from . import models
from . import forms

from django.http import HttpResponseNotFound
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth

ref = '//' + ALLOWED_HOSTS[0] + '' + '/'

menu = [
    ['Афиша', ref + theatre + paths.playbill],
    ['Новости', ref + theatre + paths.news],
    ['О театре', ref + theatre + paths.about],
    ['Посетителям', ref + theatre + paths.forVisitors],
    ['Документы', ref + theatre + paths.docs],
    ['Контакты', ref + theatre + paths.contacts],
]

def index(request):
    context = {}
    context['title'] = 'Хабаровский театр'
    context['headerTransparent'] = True
    context['menu'] = menu
    playbill = models.Schedule.objects.all()
    context['playbill'] = playbill
    news = models.News.objects.all()
    for item in news:
        if len(item.text) > 100:
            item.text = item.text[:100] + '...'
    context['news'] = news
    return render(request, 'theatre/index.html', context)

def playbill(request):
    context = {}
    context['title'] = menu[0][0]
    context['menu'] = menu
    context['menuCurrent'] = menu[0]
    if request.POST:
        form = forms.FindPlaybill(request.POST)
        context['form'] = form
        if form.is_valid():
            context['db'] = models.Schedule.objects.filter(date=form.cleaned_data['date'])
    else:
        form = forms.FindPlaybill()
        context['form'] = form

    return render(request, 'theatre/playbill.html', context)

def buyTicket(request, id):
    context = {}
    context['title'] = menu[0][0]
    context['menu'] = menu
    context['menuCurrent'] = menu[0]
    try:
        schedule = models.Schedule.objects.get(pk=id);
        context['db'] = schedule
        if request.POST and request.user.is_authenticated:
            ticket = models.Ticket()
            ticket.user = request.user
            ticket.schedule = schedule
            ticket.save()
            context['ok'] = 'Спасибо за покупку!'
    except:
        return HttpResponseNotFound()
    return render(request, 'theatre/buy_ticket.html', context)

def news(request):
    context = {}
    context['title'] = menu[1][0]
    context['menu'] = menu
    context['menuCurrent'] = menu[1]
    news = models.News.objects.all()
    for item in news:
        if len(item.text) > 500:
            item.text = item.text[:500] + '...'
    context['news'] = news
    return render(request, 'theatre/news.html', context)

def newsFull(request, id):
    context = {}
    context['title'] = menu[1][0]
    context['menu'] = menu
    context['menuCurrent'] = menu[1]
    try:
        context['news'] = models.News.objects.get(pk=id);
        context['comments'] = models.Comment.objects.filter(news=id)
    except:
        return HttpResponseNotFound()
    if request.POST and request.user.is_authenticated:
        form = forms.LeaveComment(request.POST)
        context['form'] = form
        if form.is_valid():
            comment = models.Comment()
            comment.user = request.user
            comment.news = models.News.objects.get(pk=id)
            comment.text = form.cleaned_data['text']
            comment.save()
            context['form'] = None
    else:
        context['form'] = forms.LeaveComment()
    return render(request, 'theatre/fullnews.html', context)

def about(request):
    context = {}
    context['title'] = menu[2][0]
    context['menu'] = menu
    context['menuCurrent'] = menu[2]
    return render(request, 'theatre/about.html', context)

def forVisitors(request):
    context = {}
    context['title'] = menu[3][0]
    context['menu'] = menu
    context['menuCurrent'] = menu[3]
    return render(request, 'theatre/for_visitors.html', context)

def docs(request):
    context = {}
    context['title'] = menu[4][0]
    context['menu'] = menu
    context['menuCurrent'] = menu[4]
    return render(request, 'theatre/docs.html', context)

def contacts(request):
    context = {}
    context['title'] = menu[5][0]
    context['menu'] = menu
    context['menuCurrent'] = menu[5]
    return render(request, 'theatre/contacts.html', context)

def lk(request):
    context = {}
    context['title'] = 'Личный кабинет'
    context['menu'] = menu
    if request.user.is_authenticated:
        context['user'] = request.user
        context['tickets'] = models.Ticket.objects.filter(user=request.user.pk)
    else:
        return redirect('login')
    return render(request, 'theatre/lk.html', context)

def lkUser(request, id):
    context = {}
    context['title'] = 'Личный кабинет'
    context['menu'] = menu
    try:
        context['user'] = auth.models.User.objects.get(pk=id)
    except:
        return HttpResponseNotFound()
    return render(request, 'theatre/lk.html', context)

def register(request):
    context = {}
    context['title'] = 'Регистрация'
    context['menu'] = menu
    context['button'] = 'Зарегистрироваться'
    if request.POST:
        form = UserCreationForm(request.POST)
        context['form'] = form
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('index')
    else:
        context['form'] = UserCreationForm()
    return render(request, 'theatre/auth_form.html', context)

def login(request):
    context = {}
    context['title'] = 'Вход'
    context['menu'] = menu
    context['button'] = 'Войти'
    if request.POST:
        form = AuthenticationForm(request.POST)
        context['form'] = form
        user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user:
            auth.login(request, user)
            return redirect('index')
        else:
            context['error'] = 'Неверно указано имя пользователя или пароль'
    else:
        context['form'] = AuthenticationForm()
    return render(request, 'theatre/auth_form.html', context)

def logout(request):
    auth.logout(request)
    return redirect('index')

