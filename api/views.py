from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import viewsets,permissions,generics
from rest_framework.views import APIView
from .serialize import NewUserSerializer
# from django.views.decorators.csrf import  csrf_exempt
from django.contrib.auth.models import User
from .models import NewUser
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
                                       HTTP_200_OK,
                                       HTTP_500_INTERNAL_SERVER_ERROR,
                                       HTTP_404_NOT_FOUND
)

from rest_framework.response import Response


# Create your views here.


# CHECKS THE ADMIN USERNAME AND PASSWORD(POST) IF THE GIVEN USERNAME AND PASSWORD IS CORRECT THEN GIVES TOKEN AS A OUTPUT
# POST username and password

# INPUT:
# {
#     "username":"hasher", "password":"hasher123"
# }
# Output:"token": "c95dd1cebb21e807a0c0541e7021ae62b54e00c9"(Token received)
# Rest API:http://localhost:8000/api/v1/api-token-auth


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













#New User(Sign up) Rest API code
# Post the data to the database table NewUser from models.py

# Input:    {
#              "username": "neha@mail.com",
#              "fname": "Neha",
#              "lname": "Kumari",
#              "password": "neha123"
#           }

# Rest API:http://localhost:8000/api/


class signUp(viewsets.ModelViewSet):

    queryset = NewUser.objects.all()

    # queryset = NewUser.objects.all().order_by('fname')

    permission_classes = [
        permissions.AllowAny
    ]


    serializer_class = NewUserSerializer


#GET DATA(gedata) Rest API code
# Get the data from the database table NewUser from models.py

# output:   {
#              "username": "neha@mail.com",
#              "fname": "Neha",
#              "lname": "Kumari",
#              "password": "neha123"
#           }

# REST API:http://localhost:8000/getapi

@api_view(["GET"])
@permission_classes((AllowAny,))

def getdata(request):

  queryset = NewUser.objects.all()
  serialize = NewUserSerializer(queryset , many=True)
  return Response(serialize.data)



#GET SPECIFIC DATA(getspecificdata) Rest API code
#IF WE PROVIDE THE ID IN THE URL BASED ON THAT ID WE GET THE USER INFORMATION(GET)
#REST API:http://localhost:8000/getapi/1

@api_view(["GET","POST"])
@permission_classes((AllowAny,))

def getspecificdata(request,id):
    # id=request.data.get(val)
    Newid=int(id)
    queryset = NewUser.objects.get(auto_increment_id = id)
    serialize = NewUserSerializer(queryset )
    return Response(serialize.data)
















# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def emailid(request):
#         type = request.data.get("type")
#         if type == "email":
#           email = request.data.get("email")
#           value=authenticate(email=email)
#           if value:
#             return Response( status=HTTP_200_OK)
#
#
#           else :
#
#             return Response({"Value":User.email})
#
#         # token, _ = Token.objects.get_or_create(user=Value)
#         # return Response({'token': token.key},
#         #                 status=HTTP_200_OK)
#


