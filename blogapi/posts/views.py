from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly



class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
    
    
    