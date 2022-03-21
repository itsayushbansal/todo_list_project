from rest_framework.decorators import api_view
from rest_framework.response import Response

from .permissions import has_object_permission
from .serializers import ToDoItemSerializer
from .models import ToDoItem


@api_view(['GET'])
def toDoItemList(request):
    """
    Below Function going to display all the Todo Items belonging to the user.
    """
    tasks = ToDoItem.objects.filter(user=request.user)
    serializer = ToDoItemSerializer(tasks, many=True)
    return Response({'data': serializer.data})


@api_view(['GET'])
def toDoItemDetail(request, pk):
    """
    Below Function going to display the Specific Todo Item belonging to the user.
    """
    task = ToDoItem.objects.filter(id=pk).first()
    if not task:
        return Response({'error': 'Invalid item id.'}, status=400)
    if not has_object_permission(request, task):
        return Response({'error': "You are not authorized to view this item."}, status=401)
    serializer = ToDoItemSerializer(task, many=False)
    return Response({'data': serializer.data})


@api_view(['POST'])
def toDoItemCreate(request):
    """
    Below Function going to create the Todo Item for the user.
    """
    request.data['user'] = request.user.id
    serializer = ToDoItemSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(data={'error': serializer.errors}, status=400)
    serializer.save()
    return Response({'data': serializer.data})


@api_view(['PUT'])
def toDoItemUpdate(request, pk):
    """
    Below Function going to update the Specific Todo Item's attributes belonging to the user.
    """
    task = ToDoItem.objects.filter(id=pk).first()
    if not task:
        return Response({'error': 'Invalid item id.'}, status=400)
    if not has_object_permission(request, task):
        return Response({'error': "You are not authorized to edit this item."}, status=401)
    request.data['user'] = request.user.id
    serializer = ToDoItemSerializer(instance=task, data=request.data)
    if not serializer.is_valid():
        return Response(data={'error': serializer.errors}, status=400)
    serializer.save()
    return Response({'data': serializer.data})


@api_view(['DELETE'])
def toDoItemDelete(request, pk):
    """
    Below Function going to delete a Specific Todo Item belonging to the user.
    """
    task = ToDoItem.objects.filter(id=pk).first()
    if not task:
        return Response({'error': 'Invalid item id.'}, status=400)
    if not has_object_permission(request, task):
        return Response({'error': "You are not authorized to delete this item."}, status=401)
    task.delete()
    return Response({"message": "Item deleted successfully."})
