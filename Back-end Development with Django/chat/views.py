
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user.views import UserSerializer
from chat.models import Message, Conversation
from chat.serializers import ConversationSerializer, UserIdSerializer, MessageSerializer, UpdateMessageSerializer, AddMessageSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from PIL import Image




class ConversationView(APIView):
    authentication_classes = []
    def post(self, request):
        s = ConversationSerializer(
        Conversation.objects.all(),
        many=True
    )
        return JsonResponse(
            {
            'conversations': s.data
            }
        ) 

    def get(self, request):
        s = conversations = [
            conversation.name for conversation in Conversation.objects.all()
        ]
        return Response(conversations)   


@login_required
def add_message(request): 
    s = AddMessageSerializer(
        data=request.POST,
        context={
            'user': request.user
            }
        )
    if s.is_valid():  
        s.save()
        return JsonResponse(
            {
            'message': 'Your message is saved!'
            }
        )
    else:
        return JsonResponse(
            {
            'errors': s.errors
            }, 
            status=400
        )


class MessageView(APIView):
    authentication_classes = []
    def post(self, request):
        if request.method != 'POST':
            return JsonResponse(
                {
                'message': 'Method not allowed!'
                },
            status=status.HTTP_405_METHOD_NOT_ALLOWED
            )  
             
        s = MessageSerializer(
            Message.objects.all()
            , many=True
            )
        return Response(s.data)
        

    def put(self, request):
        s = UpdateMessageSerializer(
            instance=Message.objects.get(
                id=request.data['id']
            ),
            data=request.data     
        )
        if s.is_valid():
            s.save() 
            return Response(
                {
                'message': 'Your message is updated successfully!'
                }
            )
        else:  
            return Response(
                {
                'errors': s.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )  


    def get(self, request):
        if request.method != 'GET':
            return JsonResponse(
                {
                'message': 'Method not allowed!'
                }, 
            status=status.HTTP_405_METHOD_NOT_ALLOWED)  
        if 'conversation' not in request.GET:
            return JsonResponse(
                {
                'message': 'Please send conversation id'
                },
            status=status.HTTP_400_BAD_REQUEST)    

        c = Conversation.objects.get(
            id = request.GET['conversation']
        )
        messages = Message.objects.filter(
            conversation = c
        )
        s = MessageSerializer(messages, many=True)
        return JsonResponse(
            {
            'messages': s.data
            }
        )      
        
        


   


 
        
