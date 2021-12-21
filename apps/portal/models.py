from django.db import models

# Create your models here.
class Inicial(models.Model):
    titulo = models.TextField('Título', blank = False, max_length = 255)
    texto = models.TextField('Texto', blank = False)
    botao = models.CharField('Frase-botão', blank = False, max_length = 255)
    imagem = models.ImageField(
        upload_to = 'imagens',
        verbose_name = 'Imagem',
        blank = False
    )
    descricao = models.CharField('Descrição da imagem', blank = False, max_length = 255)
    data = models.DateTimeField('Atualizado em', auto_now = True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Seção Inicial'
        verbose_name_plural = 'Seção Inicial'

class QuemSomos(models.Model):
    texto = models.TextField('Texto', blank = False)
    imagem1 = models.ImageField(
        upload_to='imagens',
        verbose_name="Primeira imagem",
        blank=False
    )
    descricao1 = models.CharField('Descrição da primeira imagem', blank=False, max_length=255)
    imagem2 = models.ImageField(
        upload_to='imagens',
        verbose_name="Segunda imagem",
        blank=False
    )
    descricao2 = models.CharField( 'Descrição da segunda imagem', blank=False, max_length=255)
    imagem3 = models.ImageField(
        upload_to='imagens',
        verbose_name="Terceira imagem",
        blank=False
    )
    descricao = models.CharField('Descrição da terceira imagem', blank=False, max_length=255)
    data = models.DateTimeField('Atualizado em', auto_now = True)

    def __str__(self):
        return self.texto

    class Meta:
        verbose_name = 'Seção Quem Somos'
        verbose_name_plural = 'Seção Quem Somos'

class SecaoEquipe(models.Model):
    titulo = models.TextField('Título', blank = False, max_length = 255)
    subtitulo = models.TextField('Subtítulo', blank = False, max_length = 255)
    data = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Seção Equipe'
        verbose_name_plural = 'Seção Equipe'

class EquipeMembro(models.Model):
    nome = models.CharField('Nome', blank = False, max_length = 255)
    imagem = models.ImageField(
        upload_to='imagens',
        verbose_name="Primeira imagem",
        blank=False
    )
    descricao = models.CharField('Descrição', blank = False, max_length = 255)
    cargo = models.CharField('Cargo',
                                blank=False, max_length=255)
    experiencia = models.CharField(
        'Experiência', blank=False, max_length=255)
    formacao = models.CharField(
        'Formação', blank=False, max_length=255)
    data = models.DateTimeField('Atualizado em', auto_now=True)
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

class Curso(models.Model):
    titulo = models.CharField('Título', blank=False, max_length=255)
    texto1 = models.TextField('Primeiro texto', blank=False)
    texto2 = models.TextField('Segundo texto', blank=False)
    texto3 = models.TextField('Terceiro texto', blank=False)
    imagem = models.ImageField(
        upload_to='imagens',
        verbose_name="Imagem",
        blank=False
    )
    descricao = models.CharField('Descrição da imagem', blank=False, max_length=255)
    link = models.CharField('Link do site', blank=True, max_length=255)
    data = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

class SecaoAprovados(models.Model):
    titulo = models.TextField('Título', blank=False, max_length=255)
    subtitulo = models.TextField('Subtítulo', blank=False, max_length=255)
    data = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Seção Aprovados'
        verbose_name_plural = 'Seção Aprovados'

class Aprovados(models.Model):
    nome = models.CharField('Nome', blank=False, max_length=255)
    instituicao = models.TextField('Instituição', blank=False, max_length=255)
    imagem = models.ImageField(
        upload_to='imagens',
        verbose_name="Imagem",
        blank=False
    )
    descricao = models.CharField('Descrição da imagem', blank=False, max_length=255)
    data = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Aprovado'
        verbose_name_plural = 'Aprovados'

class Parceiros(models.Model):
    nome = models.CharField('Nome', blank=False, max_length=255)
    imagem = models.ImageField(
        upload_to='imagens',
        verbose_name="Imagem",
        blank=False
    )
    descricao = models.CharField('Descrição da imagem', blank=False, max_length=255)
    link = models.CharField('Link de contato', blank=True, max_length=255)
    data = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Parceiro'
        verbose_name_plural = 'Parceiros'

class Contatos(models.Model):
    titulo = models.TextField('Título', blank=False, max_length=255)
    subtitulo = models.TextField('Subtítulo', blank=False, max_length=255)
    instagram = models.CharField('Instagram', blank=False, max_length=255)
    facebook = models.CharField('Facebook', blank=False, max_length=255)
    whatsapp = models.CharField('Whatsapp', blank=False, max_length=255)
    telefone1 = models.CharField('Telefone', blank=False, max_length=255)
    # telefone2 = models.CharField('Segundo telefone', blank=True, max_length=255)
    horarioM = models.CharField('Horário de funcionamento - Manhã', blank=False, max_length=255)
    horarioT = models.CharField('Horário de funcionamento - Tarde', blank=False, max_length=255)
    mapa = models.CharField('Google Maps', blank=False, max_length=500)
    data = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Contatos'
        verbose_name_plural = 'Contatos'