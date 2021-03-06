# Generated by Django 3.2.9 on 2021-11-10 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aprovados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('instituicao', models.TextField(max_length=255, verbose_name='Instituição')),
                ('imagem', models.ImageField(upload_to='imagens', verbose_name='Imagem')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição da imagem')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Aprovado',
                'verbose_name_plural': 'Aprovados',
            },
        ),
        migrations.CreateModel(
            name='Contatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=255, verbose_name='Título')),
                ('subtitulo', models.TextField(max_length=255, verbose_name='Subtítulo')),
                ('instagram', models.CharField(max_length=255, verbose_name='Instagram')),
                ('facebook', models.CharField(max_length=255, verbose_name='Facebook')),
                ('whatsapp', models.CharField(max_length=255, verbose_name='Whatsapp')),
                ('telefone1', models.CharField(max_length=255, verbose_name='Telefone')),
                ('telefone2', models.CharField(blank=True, max_length=255, verbose_name='Segundo telefone')),
                ('horarioM', models.CharField(max_length=255, verbose_name='Horário de funcionamento - Manhã')),
                ('horarioT', models.CharField(max_length=255, verbose_name='Horário de funcionamento - Tarde')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Contatos',
                'verbose_name_plural': 'Contatos',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('texto1', models.TextField(verbose_name='Primeiro texto')),
                ('texto2', models.TextField(verbose_name='Segundo texto')),
                ('texto3', models.TextField(verbose_name='Terceiro texto')),
                ('imagem', models.ImageField(upload_to='imagens', verbose_name='Imagem')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição da imagem')),
                ('link', models.CharField(blank=True, max_length=255, verbose_name='Link do site')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=255, verbose_name='Título')),
                ('subtitulo', models.TextField(max_length=255, verbose_name='Subtítulo')),
            ],
        ),
        migrations.CreateModel(
            name='Inicial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=255, verbose_name='Título')),
                ('texto', models.TextField(verbose_name='Texto')),
                ('botao', models.CharField(max_length=255, verbose_name='Frase-botão')),
                ('imagem', models.ImageField(upload_to='imagens', verbose_name='Imagem')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição da imagem')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Seção Inicial',
                'verbose_name_plural': 'Seção Inicial',
            },
        ),
        migrations.CreateModel(
            name='Parceiros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('imagem', models.ImageField(upload_to='imagens', verbose_name='Imagem')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição da imagem')),
                ('link', models.CharField(blank=True, max_length=255, verbose_name='Link de contato')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Parceiro',
                'verbose_name_plural': 'Parceiros',
            },
        ),
        migrations.CreateModel(
            name='QuemSomos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(verbose_name='Texto')),
                ('imagem1', models.ImageField(upload_to='imagens', verbose_name='Primeira imagem')),
                ('descricao1', models.CharField(max_length=255, verbose_name='Descrição da primeira imagem')),
                ('imagem2', models.ImageField(upload_to='imagens', verbose_name='Segunda imagem')),
                ('descricao2', models.CharField(max_length=255, verbose_name='Descrição da segunda imagem')),
                ('imagem3', models.ImageField(upload_to='imagens', verbose_name='Terceira imagem')),
                ('descricao3', models.CharField(max_length=255, verbose_name='Descrição da terceira imagem')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Seção Quem Somos',
                'verbose_name_plural': 'Seção Quem Somos',
            },
        ),
        migrations.CreateModel(
            name='SecaoAprovados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=255, verbose_name='Título')),
                ('subtitulo', models.TextField(max_length=255, verbose_name='Subtítulo')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Seção Aprovados',
                'verbose_name_plural': 'Seção Aprovados',
            },
        ),
    ]
