from django.http import JsonResponse
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics

from .models import Post
from .serializers import PostSerializer, PostCreateSerializer


# @api_view(['GET'])  #bez serializirsiz
# def post_list(request):
#     posts = Post.objects.all()
#     data = []
#     for i in posts:
#         post = {
#             "id": i.id,
#             "title": i.title,
#             "image": i.get_absolute_url,
#             "body": i.body,
#             "created_date": i.created_date,
#         }
#         data.append(post)
#
#     return Response(data)

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True) #many=True - bu queryset kopmarta qaytargani uchun ishlatamiz, agar detail bitta boganda kerak emas

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def detail_list(request, pk):
    try:
        posts = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise NotFound("to'pilmadi")

    serializer = PostSerializer(posts)

    return Response(serializer.data, status=status.HTTP_200_OK) # 200 ok db keladi


@api_view(['POST'])
def post_create(request):
    data = request.data  # requestdan datani oladi
    serializer = PostCreateSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def post_update(request, pk):
    try:
        instance = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise NotFound("to'pilmadi")
    data = request.data  # requestdan datani oladi
    serializer = PostCreateSerializer(instance=instance, data=data)
    serializer.is_valid(raise_exception=True) #raise exe.. true - bu agar hatolik boladigan bolsa exep qaytaradi
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PATCH'])
def post_partial_update(request, pk, **kwargs):
    try:
        instance = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise NotFound("to'pilmadi")
    #partial = kwargs.pop('partial', True) bu majburiye emas yani hech qanday malumot kemasa true db opket ddi
    partial = kwargs['partial'] = True #bu majburiy yani bitta fieldni update qiladi qoganlani qiymatini berish u-n
    data = request.data  # requestdan datani oladi
    serializer = PostCreateSerializer(instance=instance, data=data, partial=partial)
    serializer.is_valid(raise_exception=True) #raise exe.. true - bu agar hatolik boladigan bolsa exep qaytaradi
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST', 'GET']) # dekorator
def post_list_create(request):
    if request.method == "GET":
        post = Post.objects.all()
        serializer = PostCreateSerializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data  # requestdan datani oladi
    serializer = PostCreateSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def post_delete(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise NotFound("to'pilmadi")
    post.delete()
    return Response({"detail": "Succesfully deleted post"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE', 'PUT', 'PATCH', 'GET'])
def post_rud(request, pk, **kwargs):
    try:
        instance = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise NotFound("to'pilmadi")

    data = request.data

    if request.method == 'DELETE':
        instance.delete()
        return Response({"detail": "Succesfully deleted post"}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PATCH':
        partial = kwargs['partial'] = True
        serializer = PostCreateSerializer(data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'PUT':
        serializer = PostCreateSerializer(instance=instance, data=data)
        serializer.is_valid(raise_exception=True)  # raise exe.. true - bu agar hatolik boladigan bolsa exep qaytaradi
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        serializer = PostSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)