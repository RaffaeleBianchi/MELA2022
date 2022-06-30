from ast import In
from asyncore import read, write
import filecmp
import fileinput
from importlib.resources import open_text
from ntpath import altsep
from optparse import TitledHelpFormatter
from statistics import mode
from tkinter import image_names
from typing import Any, Generic
from unittest.util import _MAX_LENGTH
from urllib import response
from django.db import models
from django.forms import TextInput

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20 )

class Harry_Potter(models.Model):
    Author = models.ForeignKey(Author,on_delete=models.CASCADE)
    Title = models.CharField(max_length=50)
    pub_date = models.DateField('date published')
    
 

class The_lord_of_ring(models.Model):
    Author = models.ForeignKey(Author,on_delete=models.CASCADE)
    Title = models.CharField(max_length=40)
    pub_date = models.DateField('date published')



class The_Chronicles_of_Narnia(models.Model):
 Author = models.ForeignKey(Author,on_delete=models.CASCADE)
 Title = models.CharField(max_length=40)
 pub_date = models.DateField('date published')



class Star_War(models.Model):
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Title = models.CharField(max_length=60)
    pub_date = models.DateField('date published')



class Hunger_Game(models.Model):
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Title = models.CharField(max_length=65)
    pub_date = models.DateField(' date published')

