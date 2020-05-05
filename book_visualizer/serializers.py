from .models import Comment
from rest_framework import serializers

class GetCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('title', 'body', 'stars', 'date', 'made_by', 'based_on')

class PostCommentSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        validated_data['made_by'] = self.context['request'].user
        answer, _ = Comment.objects.update_or_create(
            made_by=validated_data['made_by'],
            based_on=validated_data['based_on'],
            defaults=validated_data
        )
        return answer

    class Meta:
        model = Comment
        fields = ('title', 'body', 'stars', 'based_on')
