# Generated by Django 4.0 on 2021-12-16 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0002_alter_agecategory_options_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='price',
            field=models.IntegerField(default=250, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]