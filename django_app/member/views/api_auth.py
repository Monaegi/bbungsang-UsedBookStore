# from django.contrib.auth import get_user_model
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#
# from member.serializers.myuser import MyUserSerializer, LogInSerializer
#
# MyUser = get_user_model()
#
# __all__ = (
#     'SignUpView',
#     'LogInView',
# )
#
#
# class SignUpView(APIView):
#     """ 회원가입 뷰 """
#
#     def post(self, request, ):
#         serializer = MyUserSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class LogInView(APIView):
#     """ 로그인 뷰 """
#
#     def post(self, request, ):
#         data = request.data.copy()
#         data['user_type'] = 'd'
#         serializer = LogInSerializer(data=data)
#
#         if serializer.is_valid(raise_exception=True):
#             return Response(serializer.validated_data)
#
