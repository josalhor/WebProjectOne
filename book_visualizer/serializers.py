from .models import Comment
from rest_framework import serializers

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
         #fields = ['title', 'body', 'stars', 'date', 'made_by', 'based_on']
