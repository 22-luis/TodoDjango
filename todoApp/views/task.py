from django.shortcuts import get_object_or_404
#constantes http
from rest_framework import status
#se encarga de devolver datos json
from rest_framework.response import Response
#clase base para crear peticiones http
from rest_framework.views import APIView
from ..models.task import Task
from ..serializers.task import TaskSerializer

class TaskList(APIView):

#obtener todas las tareas
    def get(self, request):
        task = Task.objects.all() #obtiene todas las tareas
        serializer = TaskSerializer(task, many=True) #convierte la lista de objetos en json
        return Response(serializer.data) #devuelve los datos en http

#crear una tarea
    def post(self, request):
        serializer = TaskSerializer(data=request.data) #request.data contiene los datos
        if serializer.is_valid(): #is_valid valida los datos
            serializer.save() #crea y guarda la tarea
            return Response(serializer.data, status=status.HTTP_201_CREATED) #respuesta si se creo correctamente
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #respuesta si no se pudo crear

#operaciones sobre una area segun id
class TaskDetail(APIView):

#obteer tarea
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk) #evita errores en caso de no existir
        serializer = TaskSerializer(task)
        return Response(serializer.data)

#actualizar tarea
    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#borrar tarea
    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete() #borra la tarea
        return Response(status=status.HTTP_204_NO_CONTENT) #indica que se borro con exito