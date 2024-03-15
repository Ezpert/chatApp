from django.db import models

# Create your models here.
# class Card(models.Model):
#     Basically a text field
#     word = models.CharField(max_length=200)
#


class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)




#commands for migrating the models for the database
# python manage.py makemigrations
# python manage.py migrate
