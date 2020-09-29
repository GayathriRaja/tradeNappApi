from django.shortcuts import render
from django.contrib.auth import authenticate
# from django.views.decorators.csrf import  csrf_exempt

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK

from rest_framework.response import Response


# Create your views here.


# @csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    # user=authenticate(username,password)

    # permission_classes = [
    #     permissions.AllowAny
    # ]

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
