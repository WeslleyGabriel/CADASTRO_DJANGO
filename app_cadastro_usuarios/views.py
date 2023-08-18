from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #Salvando os dados do usuario no banco.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #Exibindo todos os usuarios>
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #Agora retornamos o usuario para a pagina
    return render(request, 'usuarios/usuarios.html',usuarios)