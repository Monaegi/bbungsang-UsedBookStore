# from django.contrib.auth import authenticate, get_user_model
#
# from rest_framework import serializers
#
# from member.models import Seller
#
# MyUser = get_user_model()
#
# __all__ = (
#     'MyUserSerializer',
#     'LogInSerializer',
# )
#
#
# class MyUserSerializer(serializers.ModelSerializer):
#     """ 회원가입, 시리얼라이저 """
#
#     password = serializers.CharField(
#         label='Password',
#         write_only=True,
#     )
#     confirm_password = serializers.CharField(
#         label='Confirm Password',
#         write_only=True,
#     )
#
#     class Meta:
#         model = MyUser
#         fields = (
#             'username',
#             'password',
#             'confirm_password',
#             'my_photo',
#             'nickname',
#             'phone',
#         )
#
#     def create(self, validated_data):
#         return MyUser.objects.create_user(**validated_data)
#
#     def validate(self, data):
#         password = data.get('password', None)
#         confirm_password = data.get('confirm_password', None)
#
#         if password and password != confirm_password:
#             raise serializers.ValidationError('비밀번호가 서로 일치하지 않습니다. 다시 입력해주세요.')
#
#         # confirm_password 는 MyUser 테이블에 있는 필드가 아니므로 제외
#         data.pop('confirm_password')
#         return data
#
#
# class LogInSerializer(serializers.Serializer):
#     """ 로그인 시리얼라이저 """
#
#     username = serializers.EmailField(write_only=True, )
#     password = serializers.CharField(max_length=64, write_only=True, )
#     user_type = serializers.CharField(max_length=1, write_only=True, )
#
#     def validate(self, data):
#         username = data.get('username', None)
#         password = data.get('password', None)
#
#         user = MyUser.objects.get(username=username)
#
#         try:
#             seller = Seller.objects.get(user=user)
#             seller_pk = seller.pk
#         except Seller.DoesNotExist:
#             seller_pk = None
#
#         if data['user_type'] == 'd':
#             auth = authenticate(username=username, password=password)
#
#             if auth is None:
#                 raise serializers.ValidationError("입력하신 비밀번호가 틀립니다.")
#
#         token, created = user.get_user_token(user.pk)
#
#         ret = {
#             'token': token.key,
#             'user': {
#                 'user_pk': user.pk,
#                 'seller_pk': seller_pk,
#                 'username': username,
#             }
#         }
#         print(ret)
#         return ret