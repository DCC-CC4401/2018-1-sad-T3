from django.db import models


class Item(models.Model):
    name = models.CharField('Nombre', max_length=40)
    description = models.TextField('Descripción', blank=True)
    image = models.ImageField('Imagen del articulo', upload_to='images/items', blank=True)

    class Meta:
        abstract = True


class Action(models.Model):
    STATES = (
        ('A', 'Aceptado'),
        ('R', 'Rechazado'),
        ('P', 'Pendiente')
    )
    starting_date_time = models.DateTimeField()
    ending_date_time = models.DateTimeField()
    state = models.CharField('Estado', choices=STATES, max_length=1, default='P')
