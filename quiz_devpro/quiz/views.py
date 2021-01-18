from django.http import HttpResponse
from django.shortcuts import render, redirect

from quiz_devpro.quiz.forms import AlunoForm
from quiz_devpro.quiz.models import Pergunta, Aluno

def indice(requisicao):
    if requisicao.method == 'POST':
        email = requisicao.POST['email']
        try:
            aluno = Aluno.objects.get(email = email)
            requisicao.session['aluno_id'] = aluno.id
        except Aluno.DoesNotExist:
            form = AlunoForm(requisicao.POST)
            if form.is_valid():
                aluno = form.save
                return redirect('/perguntas/1')
            contexto = {'form': form}
            return render(requisicao, 'quiz/indice.html', contexto)
    
        else:
            requisicao.session['aluno_id'] = aluno.id
            return redirect('/perguntas/1')

    return render(requisicao, 'quiz/indice.html')


def perguntas(requisicao, indice):
    aluno_id = requisicao.session['aluno_id']
    # Mostrar a página de classificação
    pergunta = Pergunta.objects.filter(disponivel = True).order_by('id')[indice -1]

    contexto = {'indice': indice, 'pergunta': pergunta}
    if requisicao.method == 'POST':
        alternativa_escolhida = int(requisicao.POST['alternativa'])

        if alternativa_escolhida == pergunta.alternativa_correta:
            return redirect(f'/perguntas/{indice + 1}')
        contexto['alternativa_escolhida'] = alternativa_escolhida


    
    return render(requisicao, 'quiz/pergunta.html', contexto)


def classificacao(requisicao):
    return render(requisicao, 'quiz/classificacao.html')