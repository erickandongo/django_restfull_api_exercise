from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import ObjectiveSerializer, DOGSerializer
from objectives.models import Objective, DOG



@api_view(['GET'])
def objectives(request):
    objective = Objective.objects.all()
    serializer = ObjectiveSerializer(objective, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def objective_details(request, pk):
    try:
        objective_Obj = Objective.objects.get(objective_id=pk)
    except Objective.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ObjectiveSerializer(objective_Obj, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def objective_creation(request):
    serializer = ObjectiveSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

