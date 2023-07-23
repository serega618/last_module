from django.db import models
#from app_advertisements.models import Advertisement 
#a1 = Advertisement(title='Первое название',description='Первое описание',price = 100,auction = True,created_at = 0,updated_at = 0)
#a1.save()
class Advertisement(models.Model):
    title = models.CharField('заголовок',max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена',max_digits=10,decimal_places=2)
    auction = models.BooleanField('торг',help_text='Отметьте, если хотите торговаться')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
