from django.shortcuts import redirect, render
from .models import GuestUser

# Create your views here.
def registration(request):
    if request.method == 'GET':
        return render(request, 'registration.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        user = GuestUser(
            name = name,
            email = email
        )
        user.save()
        return redirect('/account/registration')