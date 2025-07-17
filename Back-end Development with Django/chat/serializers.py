from rest_framework import serializers
from chat.models import Message, Conversation
from django.contrib.auth.models import User
from user.serializers import UserSerializer




class UserIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id']


class ConversationSerializer(serializers.ModelSerializer):

    members = UserIdSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ['name', 'members']   


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['conversation','text']


class AddMessageSerializer(serializers.Serializer):
    conversation = serializers.IntegerField() 
    text = serializers.CharField(
        max_length=250,
        allow_blank=False
    )    

    def create(self, validated_data):
        c = Conversation.objects.get(
            id=validated_data['conversation'])
        m = Message(
            text = validated_data['text'], 
            sender = self.context['user'],
            conversation = c    
        )
        m.save()
        return m  


class UpdateMessageSerializer(serializers.ModelSerializer):     

    class Meta:
        model = Message
        fields = ['id','text']  

    def update(self, instance, validated_data):    
        instance.text = validated_data['text']
        instance.save()
        return instance


