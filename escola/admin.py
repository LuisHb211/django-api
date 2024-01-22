from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ('id','nome','rg','cpf','data_nascimento')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 10

# Usando o modelo de Aluno(models.py), e usando a configuracao de Alunos(admin.py)
admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id','codigo_curso','descricao','nivel')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)

# Usando o modelo de Curso(models.py), e usando a configuracao de Cursos(admin.py)
admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'periodo', 'aluno', 'curso')
    list_display_links = ('id', )
    
admin.site.register(Matricula, Matriculas)