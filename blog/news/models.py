from django.db import models


class Category(models.Model):
    name = models.CharField('Nazwa Kategorii', max_length=100)
    

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def __unicode__(self):
        return self.name


class News(models.Model):
    title = models.CharField('Tytul', max_length=255)
    Tresc = models.TextField()
    release_date = models.DateField()
    time_date = models.TimeField()

    
    class Meta:
        verbose_name = "Wiadomosc"
        verbose_name_plural = "Wiadomosci"

    def __unicode__(self):
        return self.title
