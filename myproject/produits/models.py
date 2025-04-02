from django.db import models


class  Bureau(models.Model):
    image = models.ImageField(upload_to='photos')
class  Chambre(models.Model):
    image = models.ImageField(upload_to='photos')
class  Salon(models.Model):
    image = models.ImageField(upload_to='photos')