from django import forms
from .choices import *
from .mails import send_mail_template
from django.conf import settings

class FormContato(forms.Form):

    nome = forms.CharField(
        label='Nome',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome...'})
    )
    telefone = forms.CharField(
        label='Telefone',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu telefone...'})
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu e-mail...'})
    )
    curso = forms.CharField(
        label='Curso',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu curso...'})
    )
    mensagem = forms.CharField(
        label='Mensagem/Dúvida',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite sua mensagem...'})
    )

    def send_mail(self):
        subject = 'Mensagem de %s' % self.cleaned_data['email']
        context = {
            'nome': self.cleaned_data['nome'],
            'telefone': self.cleaned_data['telefone'],
            'email': self.cleaned_data['email'],
            'curso': self.cleaned_data['curso'],
            'mensagem': self.cleaned_data['mensagem'],
        }

        send_mail_template(
            subject,
            'contato_email.html',
            context,
            [settings.CONTACT_EMAIL]
        )


class FormMatricula(forms.Form):
    #informações do Aluno
    nome_aluno = forms.CharField(
        label='Nome',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome...'})
    )
    endereco = forms.CharField(
        label='Endereço',
        max_length=300,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu endereço...' })
    )
    telefone_aluno = forms.CharField(
        label='Telefone',
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu telefone...'})
    )
    email_aluno = forms.EmailField(
        label='E-mail',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o email...'})
    )
    escola = forms.CharField(
        label='Escola de origem',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a escola...'})
    )
    periodo = forms.CharField(
        label='Período',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o seu período...'})
    )
    curso = forms.ChoiceField(
        choices=CURSOS, label='Curso',
        widget=forms.Select(),
        required=True
    )
    rg_aluno = forms.CharField(
        label='RG',
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu RG...'})
    )
    cpf_aluno = forms.CharField(
        label='CPF',
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu CPF...'})
    )
    indicacao = forms.CharField(
        label='Indicação',
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite como conheceu...'})
    )
    blusa = forms.ChoiceField(
        label='Tamanho da blusa',
        choices=BLUSAS,
        required=True
    )

    #Responsável
    nome_responsavel = forms.CharField(
        label='Nome completo',
        required=True,
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do responsável...'})
    )
    telefone_responsavel = forms.CharField(
        label='Telefone',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o telefone do responsável...'})
    )
    email_responsavel = forms.EmailField(
        label='E-mail',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o e-mail do reponsável...'})
    )
    rg_responsavel = forms.CharField(
        label='RG',
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o RG do responsável...'})
    )
    cpf_responsavel = forms.CharField(
        label='CPF',
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o CPF do responsável...'})
    )

    def send_mail(self):
        subject = 'Solicitação de Matrícula de %s' % self.cleaned_data['nome_aluno']
        context = {
            'nome_aluno': self.cleaned_data['nome_aluno'],
            'telefone_aluno': self.cleaned_data['telefone_aluno'],
            'email_aluno': self.cleaned_data['email_aluno'],
            'curso': self.cleaned_data['curso'],
            'endereco': self.cleaned_data['endereco'],
            'escola': self.cleaned_data['escola'],
            'periodo': self.cleaned_data['periodo'],
            'rg_aluno': self.cleaned_data['rg_aluno'],
            'cpf_aluno': self.cleaned_data['cpf_aluno'],
            'indicacao': self.cleaned_data['indicacao'],
            'blusa': self.cleaned_data['blusa'],
            'nome_responsavel': self.cleaned_data['nome_responsavel'],
            'telefone_responsavel': self.cleaned_data['telefone_responsavel'],
            'email_responsavel': self.cleaned_data['telefone_responsavel'],
            'rg_responsavel': self.cleaned_data['rg_responsavel'],
            'cpf_responsavel': self.cleaned_data['cpf_responsavel'],
        }

        send_mail_template(
            subject,
            'matricula_email.html',
            context,
            [settings.CONTACT_EMAIL]
        )