from django.shortcuts import render

from .forms import FormMatricula, FormContato
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from .models import EquipeMembro, Inicial, QuemSomos, SecaoEquipe, Curso, SecaoAprovados, Aprovados, Parceiros, Contatos

# Create your views here.
def index(request):

    if request.method == 'POST':
        form = FormContato(request.POST)
        if form.is_valid():
            try:
                form.send_mail()
                form = FormContato()
                messages.success(request, 'Enviado com sucesso!')
            except:
                messages.error(request, 'Erro ao enviar! Tente novamente!')
            
            return HttpResponseRedirect(reverse('index') + '#contato')
    else:
        form = FormContato()


    inicial = Inicial.objects.last()
    quem_somos = QuemSomos.objects.last()
    secao_equipe = SecaoEquipe.objects.last()
    equipes = EquipeMembro.objects.all()[:4]
    cursos = Curso.objects.all()
    secao_aprovados = SecaoAprovados.objects.last()
    aprovados = Aprovados.objects.all()
    parceiros = Parceiros.objects.all()
    contatos = Contatos.objects.last()

    context = {
        'inicial': inicial,
        'quem_somos': quem_somos,
        'secao_equipe': secao_equipe,
        'equipes': equipes,
        'cursos': cursos,
        'secao_aprovados': secao_aprovados,
        'aprovados': aprovados,
        'parceiros': parceiros,
        'contatos': contatos,
        'form': form,
    }
    return render(request, 'index.html', context)

def matricula(request):
    if request.method == 'POST':
        form = FormMatricula(request.POST)
        if form.is_valid():
            try: 
                form.send_mail()
                form = FormMatricula()
                messages.success(request, 'Enviado com sucesso!')
            except:
                messages.error(request, 'Erro ao enviar! Tente novamente!')
            return HttpResponseRedirect(reverse('matricula'))
    else:
        form = FormMatricula()

    contatos = Contatos.objects.last()
    context = {'form' : form, 'contatos': contatos}
    return render(request, 'matricula.html', context)

def error_404_view(request, exception):
    contatos = Contatos.objects.last()
    context = {'contatos': contatos}
    return render(request, '404.html', context)