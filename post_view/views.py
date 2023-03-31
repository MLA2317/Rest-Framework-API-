from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from .models import Post
from .serializer import PostSerializer


class PostListView(views.APIView):

    def get(self, request, *args, **kwargs):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostRetrieveView(views.APIView):

    def get(self, request, pk, *args, **kwargs):
        instance = Post.objects.get(id=pk)
        serializer = PostSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostUpdateView(views.APIView):

    def put(self, request, pk, *args, **kwargs):
        data = request.data
        instance = Post.objects.get(id=pk)
        serializer = PostSerializer(data=data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostPartialView(views.APIView):

    def patch(self, request, pk, *args, **kwargs):
        data = request.data
        instance = Post.objects.get(id=pk)
        serializer = PostSerializer(data=data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDeleteView(views.APIView):

    def delete(self, request, pk, *args, **kwargs):
        instance = Post.objects.get(id=pk)
        instance.delete()
        return Response({"detail": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT)


class PostListCreateView(views.APIView):

    def get(self, request, *args, **kwargs):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostRUDView(views.APIView):

    def get(self, request, pk, *args, **kwargs):
        instance = Post.objects.get(id=pk)
        serializer = PostSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        data = request.data
        instance = Post.objects.get(id=pk)
        serializer = PostSerializer(data=data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        data = request.data
        instance = Post.objects.get(id=pk)
        serializer = PostSerializer(data=data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        instance = Post.objects.get(id=pk)
        instance.delete()
        return Response({"detail": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
