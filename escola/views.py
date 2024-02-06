from rest_framework import viewsets, generics, status
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, AlunoSerializerV2,CursoSerializer, MatriculaSerializer, ListaMatriculaAlunoSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class AlunosViewSet(viewsets.ModelViewSet):
    '''
    Exibe todos os alunos e alunas
    '''
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    '''
    Autenticacao para verificar se o usuario esta logado como um dos usuarios disponiveis/superuser
    '''
    
    # Funcao para verificar qual serializer sera passado, o V1 ou V2 
    def get_serializer_class(self):
        if self.request.version == 'V2':
            return AlunoSerializerV2
        else:
            return AlunoSerializer
    
class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    #Limitando as funcoes disponiveis para todo usuario que entrar
    http_method_names = ['get','post','put','path']
    
    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        return super(MatriculaViewSet, self).dispatch(*args, **kwargs)
    
    
class ListaMatriculasAluno(generics.ListAPIView):
    """
    Uma API de visualização genérica para listar as matrículas de um aluno específico.
    Esta classe utiliza o Django Rest Framework para criar uma view que retorna todas as
    matriculas associadas a um aluno, identificado pelo parâmetro 'pk' (primary key) na URL.

    Atributos:
    - queryset: Define o conjunto de consultas para recuperar as matrículas do aluno com base
      no 'pk' fornecido na URL.
    - serializer_class: Define a classe serializadora a ser usada para converter os objetos Matricula
      em representações JSON.
    """
    def get_queryset(self):
        """
        Retorna o conjunto de consultas para obter as matrículas do aluno com base no 'pk' fornecido na URL.
        """
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculaAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
