from django.shortcuts import render

# Create your views here.



# for login
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LoginSerializer

@api_view(['POST'])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        token = serializer.validated_data['token']
        return Response({"token": token}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

###




# for mypage
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mypage(request):
    content = {'message': '반갑습니다,' + str(request.user.username) + '님!'}
    
    return Response(content)

###





# for logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        request.user.auth_token.delete()
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"success": "Successfully logged out."}, status=status.HTTP_200_OK)

###


