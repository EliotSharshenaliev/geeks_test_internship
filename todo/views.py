from rest_framework import generics
from todo.models import Todo
from todo.serializers import TodoSerializer


class TodosListAPIView(generics.ListAPIView):
    """ Для получения задач в списке"""
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class TodoRetrieveAPIView(generics.RetrieveAPIView):
    """ Для получения задач по Id"""
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class TodoCreateAPIView(generics.CreateAPIView):
    """ Для создания задачи"""
    serializer_class = TodoSerializer


class TodoUpdateAPIView(generics.UpdateAPIView):
    """ Для обновние задач по id"""
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class TodoDestroyAPIView(generics.DestroyAPIView):
    """ Для удаления задач по id"""
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
