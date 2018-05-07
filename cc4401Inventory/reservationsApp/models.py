from mainApp.models import Action
from spacesApp.models import Space
from django.db import models


class Reservation(Action):
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
