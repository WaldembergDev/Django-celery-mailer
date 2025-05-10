from django.shortcuts import redirect, render
from .models import GuestUser
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
def registration(request):
    # verificando se é uma requisição do tipo GET
    if request.method == 'GET':
        return render(request, 'registration.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        # validando os campos nome e email
        if not name or not email:
            messages.add_message(request, constants.WARNING, 'É necessário que nome e email estão preenchidos!')
            return redirect('/account/registration')
        # criando um user
        user = GuestUser(
            name = name,
            email = email
        )
        # salvando o user no banco de dados
        user.save()
        # adicionando uma mensagem ao django message
        messages.add_message(request, constants.SUCCESS, 'Registro realizado com sucesso!')
        # redirecionando para a mesma página com a mensagem de feedback
        return redirect('/account/registration')