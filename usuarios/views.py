from unicodedata import name
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib import auth


@csrf_protect
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            print('Campo Vazio!')
            return redirect('cadastro')
        if not email.strip():
            print('Campo Vazio!')
            return redirect('cadastro')
        if not senha != senha2:
            pass
        if User.objects.filter(email=email).exists():
            print('Usuario já cadastrado')
            return redirect('cadastro')

        user = User.objects.create_user(
            username=nome, email=email, password=senha)
        user.save()
        print('Usurio cadastrado com sucesso!!')
        return redirect('login')

    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == '':
            print('Campos Invalidos')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(
                email=email).values_list('username', flat=True)
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('login')
                return redirect('dashboard')

    return render(request, 'usuarios/login.html')


def dashboard(request):
    return render(request, 'usuarios/dashboard.html')


def logout(request):
    pass
