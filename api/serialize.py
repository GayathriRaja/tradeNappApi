from rest_framework import serializers
from .models import NewUser



class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ("auto_increment_id","username","fname","lname")
