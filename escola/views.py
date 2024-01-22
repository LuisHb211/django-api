from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaAlunoSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
    '''
    Exibe todos os alunos e alunas
    '''
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    '''
    Autenticacao para verificar se o usuario esta logado como um dos usuarios disponiveis/superuser
    '''
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
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
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaAlunosMatriculados(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]           