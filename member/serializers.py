from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=100)
    university = serializers.CharField(max_length=50)
    location = serializers.CharField(max_length=200)
    
    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'university': self.validated_data.get('university', ''),
            'location': self.validated_data.get('location', ''),
        }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.username = self.cleaned_data.get('username')
        user.nickname = self.cleaned_data.get('nickname')
        user.university = self.cleaned_data.get('university')
        user.location = self.cleaned_data.get('location')
        user.save()
        adapter.save_user(request, user, self)
        return user



from .models import CustomUser

class CustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'nickname', 'university', 'location']






# # for login

# # users/serializers.py
# from django.contrib.auth import authenticate
# # Django의 기본 authenticate 함수 -> 우리가 설정한 DefaultAuthBackend인 TokenAuth 방식으로 유저를 인증해준다.

# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(required=True, write_only=True)
#     # write_only=True 옵션을 통해 클라이언트->서버의 역직렬화는 가능하지만, 서버->클라이언트 방향의 직렬화는 불가능하도록 해준다.
    
#     def validate(self, data):
#         user = authenticate(**data)
#         if user:
#             token = CustomUser.objects.get(user=user) # 해당 유저의 토큰을 불러옴
#             return token
#         raise serializers.ValidationError( # 가입된 유저가 없을 경우
#             {"error": "Unable to log in with provided credentials."}
#         )
###


# for login
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import CustomUser

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            return {'token': token.key}
        raise serializers.ValidationError(
            {"error": "Unable to log in with provided credentials."}
        )



###


# 내가 한 거
# from .models import CustomUser

# class LoginSerializer(serializers.ModelSerializer):

#     class Meta:
#         model=CustomUser

#         fields=['id','Username','Password1']










# ############
# # test


# # serializers.py

# from rest_framework import serializers
# from .models import Board

# class BoardSerializer(serializers.ModelSerializer):
#     author_nickname = serializers.SerializerMethodField()

#     class Meta:
#         model = Board
#         fields = ['id', 'title', 'content', 'author', 'author_nickname', 'created_at', 'updated_at']

#     def get_author_nickname(self, obj):
#         return obj.author.nickname  # 이 부분에서 obj.author에는 Member 인스턴스가 있어야 합니다.




# #############


# # 닉네임 구현