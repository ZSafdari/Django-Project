from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from django.http import JsonResponse
from user.serializers import RequestSignUpSerializer, RequestLoginSerializer, UserSerializer, UpdateProfileSerializer




class SignUpView(APIView):
    authentication_classes = []
    def post(self, request):
        s = RequestSignUpSerializer(data=request.data)
        if s.is_valid():
            u = s.save()
            return Response(
                {
                'message': 'Your account is created successfuly!',
                'data': s.data
                }
            )
        return Response(
            s.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LoginView(APIView):
    authentication_classes = []
    def post(self, request):
        s = RequestLoginSerializer(
            data=request.data
        )
        if s.is_valid():
            u = authenticate(
                request,
                username=s.data['username'],
                password=s.data['password']
            )
            if u is None:
                return Response(
                    {
                        'message': 'Account not found!'
                    }, 
                    status=status.HTTP_404_NOT_FOUND
                ) 
            if u:
                login(request, u)
                return Response(
                    {
                        'message': 'Your account information is correct!',
                        'data': {
                            'id': u.id,
                            'first_name': u.first_name,
                            'last_name': u.last_name,
                            'username': u.username,
                            'email': u.email   
                        }
                    }, 
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'message': 'Wrong Username or Password!'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response(
                s.errors,
                status=status.HTTP_400_BAD_REQUEST
            )          


class UpdateProfileView(APIView): 
    authentication_classes = []       
    def put(self, request):  
        s = UpdateProfileSerializer(
            instance=User.objects.get(
                id=request.data['id']
            ),
            data=request.data
        )
        if s.is_valid():
            s.save() 
            return Response(
                {
                'message': 'Your Profile is updated successfully!'
                }
            )
        else:  
            return Response(
                {
                'errors': s.errors
                }, 
                status=status.HTTP_400_BAD_REQUEST
            ) 


class UsersListView(APIView):
    authentication_classes = []
    #type1: (just a list of usernames + less code lines! ^.^)b )
    def get(self, request):
        usernames = [
            user.username for user in User.objects.all()
        ]
        return Response(usernames)

    #type2: (a list of dictionaries with users' fullnames!)
    # def get(self, request):
    #     s = UserSerializer(
    #     User.objects.all(),
    #     many=True
    # )
    #     return JsonResponse(
    #         {
    #         'List of Users': s.data
    #         }
    # )    




        
