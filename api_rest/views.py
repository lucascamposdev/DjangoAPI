from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def get_users(request):

    if request.method == 'GET':

        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_by_nickname(request, nick):

    try:
        user = User.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':

        serializer = UserSerializer(user)
        return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):

    if request.method == 'GET':

        try:
            if request.GET['user']:
                user_nickname = request.GET['user']
                
                try:
                    user = User.objects.get(pk=user_nickname)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                serializer = UserSerializer(user)
                return Response(serializer.data)
            
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)