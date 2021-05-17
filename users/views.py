from rest_framework import status as s
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, logout, authenticate
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView

class login_user(APIView):
    serializer_class = UserSerializer
    def post(self,request):
        data = request.data
        user_name = data['username']
        pass_word = data['password']
        user = authenticate(request,username=user_name,password=pass_word)
        if user:
            login(request,user)
            return Response(UserSerializer(instance=user).data)
        else:
            return Response({'err': 'Invalid credentials'}, status=s.HTTP_403_FORBIDDEN)


class logout_user(APIView):
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self,request):
        logout(request)
        return Response()


class status(APIView):
    serializer_class = UserSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self,request):
        user = UserSerializer(instance=request.user)
        return Response(user.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_user(request: Request) -> Response:
    """
    Search user by query.
    """
    if not request.query_params.get('query'):
        return Response({'type': 'error', 'data': {'message': 'Invalid username query'}})

    users = User.objects.filter(
        username__contains=request.query_params.get('query'))
    return Response(UserSerializer(instance=users, many=True).data)
