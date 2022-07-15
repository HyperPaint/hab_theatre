from django.contrib import admin

from . import models

class Show(admin.ModelAdmin):
    list_display = ['pk', 'title', 'type', 'ageCategory']
    list_display_links = ['pk']
    search_fields = ['title', 'type', 'ageCategory']

admin.site.register(models.Show, Show)

class ShowType(admin.ModelAdmin):
    list_display = ['pk', 'title']
    list_display_links = ['pk']
    search_fields = ['title']

admin.site.register(models.ShowType, ShowType)

class AgeCategory(admin.ModelAdmin):
    list_display = ['pk', 'age']
    list_display_links = ['pk']
    search_fields = ['age']

admin.site.register(models.AgeCategory, AgeCategory)

class Schedule(admin.ModelAdmin):
    list_display = ['pk', 'show', 'date', 'time']
    list_display_links = ['pk']
    search_fields = ['show', 'date', 'time']

admin.site.register(models.Schedule, Schedule)

class Ticket(admin.ModelAdmin):
    list_display = ['pk', 'user', 'schedule']
    list_display_links = ['pk']
    search_fields = ['user', 'schedule']

admin.site.register(models.Ticket, Ticket)

class News(admin.ModelAdmin):
    list_display = ['pk', 'title']
    list_display_links = ['pk']
    search_fields = ['title']

admin.site.register(models.News, News)

class Comment(admin.ModelAdmin):
    list_display = ['pk', 'user', 'news']
    list_display_links = ['pk']
    search_fields = ['user', 'news']

admin.site.register(models.Comment, Comment)
