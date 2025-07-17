from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password




class UserSerializer(serializers.ModelSerializer):

    fullname = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['fullname']

    def get_fullname(self, obj):
        return obj.get_full_name()  


class RequestSignUpSerializer(serializers.ModelSerializer):
   
    class Meta():
        model = User
        fields = '__all__'
 

    def create(self, data):
        u = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            username=data['username'],
            password=data['password'],
            email=data['email']
        )
        u.set_password(data['password'])
        u.save()
        return u
 


class RequestLoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True, max_length=30, allow_blank=False,
    )
    password = serializers.CharField(
        required=True, max_length=30, allow_blank=False 
    )

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.post('password')
        )
        return validated_data 
    

    def validated_password(self, data):
        if data != request.data['password']: 
            raise serializers.ValidationError(
                "Your password in not validated!"
            )
        return data             


class UpdateProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id", "first_name" , "last_name"]

    def update(self, instance, validated_data):    
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.save()
        return instance         
        


