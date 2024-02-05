from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

'''
o serializer.py é uma espécie de ponte entre as nossas informações escritas em Python e em Json. 
Os dados em Python serão transformados em Json, e os em Json, transformados em Python para salvar no banco de dados.
'''

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Aluno
        fields = ['id','nome','rg','cpf','data_nascimento']
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
        
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []
        
class ListaMatriculaAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo =   serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    ''' 
    source eh usado para indicar de onde o valor do caimpo deve ser retrado no objeto que esta sendo serializado. 
    Neste caso, aluno_nome eh obtido a partir do atributo nome do relacionamento alunos da instancia de Matricula. 
    ''' 
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome', ]
        
# Sera o novo serializer da versao 2, a diferenca para o V1 eh o celular
class AlunoSerializerV2(serializers.ModelSerializer):
    class Meta:
        model  = Aluno
        fields = ['id','nome','rg','cpf','data_nascimento','celular']
        