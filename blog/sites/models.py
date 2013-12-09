from django.db import models

class Chujostwo(models.Model):
	size = models.CharField('Rozmiar', max_length = 15)
	age = models.TextField()