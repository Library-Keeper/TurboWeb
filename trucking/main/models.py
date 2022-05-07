from django.db import models

class Review(models.Model):
    name = models.CharField('Имя', max_length=50)
    email = models.CharField('E-Mail', max_length=250)
    rev = models.TextField('Отзыв')


    def __str__(self):
        pass
