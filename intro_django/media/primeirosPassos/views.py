from django.shortcuts import render
from .models import Pessoa
# Create your views here.

def listar_registros(request):
    pessoa = Pessoa.objects.all()
    return render(request, 'list.html', {'pessoa': pessoa})
