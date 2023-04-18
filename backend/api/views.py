from blog.models import Article
from django.contrib.auth.models import User
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .permissions import (IsAuthorOrReadOnly, IsStaffOrReadOnly,
                          IsSuperUserOrStaffReadOnly)
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)


'''
class RevokeToken(APIView):
    permission_classes = (IsAuthenticated,)
    
    def delete(self, request):
        request.auth.delete()
        return Response({'detail': 'Token revoked successfully.'}, status=204)
'''
