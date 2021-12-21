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
        label='Nome completo do Aluno',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome...'})
    )
    endereco = forms.CharField(
        label='Endereço completo',
        max_length=300,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu endereço...' })
    )
    telefone_aluno = forms.CharField(
        label='Contato do aluno',
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu telefone...'})
    )
    email_aluno = forms.EmailField(
        label='E-mail',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o email...'})
    )
    tem_whatsapp = forms.ChoiceField(
        label='Esse número tem Whatsapp?',
        choices=HAS_WPP,
        required=True
    )
    data_nascimento = forms.CharField(
        label='Data de nascimento',
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a data...'})
    )
    escola = forms.CharField(
        label='Escola que frequenta atualmente',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a escola...'})
    )
    periodo = forms.CharField(
        label='Série de ensino',
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
        label='Quem indicou o Cursinho:',
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite como conheceu...'})
    )
    blusa = forms.ChoiceField(
        label='Tamanho da blusa',
        choices=BLUSAS,
        required=True
    )
    nome_pai = forms.CharField(
        label='Nome completo do pai',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do pai...'})
    )
    nome_mae = forms.CharField(
        label='Nome completo da mãe',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome da mãe...'})
    )
    telefone_pai = forms.CharField(
        label='Contato do pai',
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o telefone do pai...'})
    )
    telefone_mae = forms.CharField(
        label='Contato da mãe',
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o telefone da mãe...'})
    )

    #Responsável
    nome_responsavel = forms.CharField(
        label='Nome completo',
        required=True,
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do responsável...'})
    )
    telefone_responsavel = forms.CharField(
        label='Contato',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o telefone do responsável...'})
    )
    tem_whatsapp_responsavel = forms.ChoiceField(
        label='Esse número tem Whatsapp?',
        choices=HAS_WPP,
        required=True
    )
    email_responsavel = forms.EmailField(
        label='E-mail',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o e-mail do reponsável...'})
    )
    endereco_responsavel = forms.CharField(
        label='Endereço completo',
        max_length=300,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu endereço...' })
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
            'endereco': self.cleaned_data['endereco'],
            'telefone_aluno': self.cleaned_data['telefone_aluno'],
            'email_aluno': self.cleaned_data['email_aluno'],
            'tem_whatsapp': self.cleaned_data['tem_whatsapp'],
            'data_nascimento': self.cleaned_data['data_nascimento'],
            'escola': self.cleaned_data['escola'],
            'periodo': self.cleaned_data['periodo'],
            'curso': self.cleaned_data['curso'],
            'rg_aluno': self.cleaned_data['rg_aluno'],
            'cpf_aluno': self.cleaned_data['cpf_aluno'],
            'indicacao': self.cleaned_data['indicacao'],
            'blusa': self.cleaned_data['blusa'],
            'nome_pai': self.cleaned_data['nome_pai'],
            'nome_mae': self.cleaned_data['nome_mae'],
            'telefone_pai': self.cleaned_data['telefone_pai'],
            'telefone_mae': self.cleaned_data['telefone_mae'],

            'nome_responsavel': self.cleaned_data['nome_responsavel'],
            'telefone_responsavel': self.cleaned_data['telefone_responsavel'],
            'tem_whatsapp_responsavel': self.cleaned_data['tem_whatsapp_responsavel'],
            'email_responsavel': self.cleaned_data['email_responsavel'],
            'endereco_responsavel': self.cleaned_data['endereco_responsavel'],
            'rg_responsavel': self.cleaned_data['rg_responsavel'],
            'cpf_responsavel': self.cleaned_data['cpf_responsavel'],
        }

        send_mail_template(
            subject,
            'matricula_email.html',
            context,
            [settings.CONTACT_EMAIL]
        )