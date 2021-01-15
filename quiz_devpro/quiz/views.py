from django.http import HttpResponse
from django.shortcuts import render, redirect

from quiz_devpro.quiz.forms import AlunoForm
from quiz_devpro.quiz.models import Pergunta

def indice(requisicao):
    if requisicao.method == 'POST':
        email = requisicao.POST['email']
        try:
            aluno = Aluno.objects.get(email=email)
        except Aluno.DoesNotExist:
        requisicao.session['aluno_id'] = aluno.id
        return redirect('/perguntas/1')

        form = AlunoForm(requisicao.POST)
        if form.is_valid():
            aluno = form.save
            return redirect('/perguntas/1')
        contexto = {'form': form}

    return render(requisicao, 'quiz/indice.html')


def perguntas(requisicao, indice):
    aluno_id = requisicao.session['aluno_id']
    pergunta = Pergunta.objects.filter(disponivel = True).order_by('id')[indice -1]
    contexto = {'indice': indice, 'pergunta': pergunta}
    return render(requisicao, 'quiz/pergunta.html', contexto)


def classificacao(requisicao):
    return render(requisicao, 'quiz/classificacao.html')