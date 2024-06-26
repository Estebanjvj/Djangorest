from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer #, TestUserSerializer

@api_view(['GET','POST'])
def user_api_view(request):

    # List
    if request.method == 'GET':
        users = User.objects.all().values('id','username','email','name','last_name','password')
        users_serializers = UserListSerializer(users, many=True)
        return Response(users_serializers.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_detail_api_view(request, pk=None):
    user = User.objects.filter(id=pk).first()
    if user:
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        # Update
        elif request.method == 'PUT':

            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'Eliminado'}, status=status.HTTP_200_OK)
    else:
        return Response({'message':'Usuario no encontrado'}, status=status.HTTP_400_BAD_REQUEST)
