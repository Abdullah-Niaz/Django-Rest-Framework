import re
from rest_framework import serializers
from .models import Todo
from django.utils.text import slugify


class TodoSerailizer(serializers.ModelSerializer):
    
    slug = serializers.SerializerMethodField()
    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ['title','slug', 'description', 'is_done', 'uid']

    def get_slug(self,obj):
        return slugify(obj.title)


    # def validate(self, validated_data):
    #     print(validated_data)
    #     title = validated_data.get('title')

    #     if title.is_valid():
    #         print("valid")
    #         pattern = re.compile(r'[^a-zA-Z0-9\s]')
    #         if pattern.search(title):
    #             raise serializers.ValidationError(
    #                 "Todo Title cannot contain special characters")

    #     return validated_data

