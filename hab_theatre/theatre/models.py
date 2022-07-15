from django.db import models
from django.contrib.auth.models import User

class Show(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    type = models.ForeignKey('ShowType', models.CASCADE, verbose_name='Жанр')
    ageCategory = models.ForeignKey('AgeCategory', models.CASCADE, verbose_name='Возрастная категория')
    price = models.IntegerField(verbose_name='Цена')
    about = models.TextField(max_length=1000, verbose_name='О постановке')
    img = models.ImageField(verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Постановка'
        verbose_name_plural = 'Постановки'

class ShowType(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class AgeCategory(models.Model):
    age = models.IntegerField(unique=True, verbose_name='Возраст')

    def __str__(self):
        return str(self.age) + '+'

    class Meta:
        verbose_name = 'Возрастная категория'
        verbose_name_plural = 'Возрастные категории'

class Schedule(models.Model):  # poster
    show = models.ForeignKey('Show', models.CASCADE, verbose_name='Постановка')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')

    def __str__(self):
        return str(self.show) + ' ' + str(self.date) + ' ' + str(self.time)

    class Meta:
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеансы'

class Ticket(models.Model):
    user = models.ForeignKey(User, models.CASCADE, verbose_name='Пользователь')
    schedule = models.ForeignKey('Schedule', models.CASCADE, verbose_name='Сеанс')

    def __str__(self):
        return str(self.user) + ' ' + str(self.schedule)

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    text = models.TextField(max_length=1000, verbose_name='Текст')
    img = models.ImageField(verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Comment(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, null=True, verbose_name='Пользователь')
    news = models.ForeignKey('News', models.CASCADE, verbose_name='Новость')
    text = models.TextField(max_length=1000, verbose_name='Текст')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
