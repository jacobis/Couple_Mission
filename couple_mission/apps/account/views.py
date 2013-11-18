from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from couple_mission.apps.account.models import UaiUser
from couple_mission.apps.account.serializers import AccountSerializer

@api_view(['GET', 'POST'])
def user_list(request, foramt=None):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        users = UaiUser.objects.all()
        serializer = AccountSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AccountSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk, format=None):
    """
    Retrieve, update or delete a user instance
    """
    try:
        user = UaiUser.objects.get(pk=pk)
    except UaiUser.DoseNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AccountSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status==status.HTTP_202_NO_CONTENT)
