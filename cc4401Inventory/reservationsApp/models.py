from mainApp.models import Action


class Reservation(Action):

    class Meta:
        proxy = True
