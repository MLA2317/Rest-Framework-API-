from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'body', 'created_date']

    def validate(self, attrs): # kirgizvotkan malumotimizni tekshiradi
        title = attrs.get('title')
        body = attrs.get('body', None)
        if title and title.islower():
            raise ValidationError({"title": 'first letter of title must be uppercase'})
        if body and len(body) < 10:
            raise ValidationError({"body": 'body must be greater than 10 letter'})
        return attrs
