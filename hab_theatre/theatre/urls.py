from django.urls import path

from . import paths
from . import views

urlpatterns = [
    path(paths.index, views.index, name="index"),

    path(paths.playbill, views.playbill, name="playbill"),
    path(paths.playbillRoot + '<int:id>', views.buyTicket),
    path(paths.news, views.news, name="news"),
    path(paths.newsRoot + '<int:id>', views.newsFull),
    path(paths.about, views.about, name="about"),
    path(paths.forVisitors, views.forVisitors, name="forVisitors"),
    path(paths.docs, views.docs, name="docs"),
    path(paths.contacts, views.contacts, name="contacts"),

    path(paths.lk, views.lk, name='lk'),
    path(paths.lkRoot + '<int:id>', views.lkUser),

    path(paths.register, views.register, name="register"),
    path(paths.login, views.login, name="login"),
    path(paths.logout, views.logout, name="logout"),
]
