from django.shortcuts import render, redirect
from .models import Reservation


def delete(request):
    if request.method == 'POST':
        reservation_id = request.POST['reservation_id']
        try:
            reservation = Reservation.objects.get(id=reservation_id)
            reservation.delete()
            return redirect('user_data', user_id=request.user.id)
        except:
            return redirect('user_data', user_id=request.user.id)
