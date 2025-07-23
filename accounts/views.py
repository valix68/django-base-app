from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# Logout chỉ đơn giản phía client xóa token, nếu muốn revoke thì phải lưu blacklist token
from rest_framework.views import APIView
class LogoutView(APIView):
    def post(self, request):
        # SimpleJWT không lưu session, logout chỉ cần client xóa token
        return Response({"message": "Logged out. Please delete token on client."}, status=status.HTTP_200_OK)
