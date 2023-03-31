from rest_framework import viewsets
from .serializer import PostViewSetSerializer
from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostViewSetSerializer
