from django.forms import ModelForm
# Falta importar algo aqui


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email']