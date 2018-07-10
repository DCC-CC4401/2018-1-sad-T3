from django.shortcuts import render, redirect
from .models import Reservation
from django.contrib import messages


def delete(request):
    if request.method == 'POST':
        reservation_id = request.POST['reservation_id']
        try:
            messages.success(request, 'Reserva eliminada con éxito')
            reservation = Reservation.objects.get(id=reservation_id)
            reservation.delete()
            return redirect('user_data', user_id=request.user.id)
        except:
            messages.warning(request, 'Ha ocurrido un error y la reserva no se ha eliminado')
            return redirect('user_data', user_id=request.user.id)
