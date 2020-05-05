from .models import Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        user = self.context['request'].user
        if attrs['made_by'] != user and not user.is_staff:
            raise serializers.ValidationError('You cannot post for another user')
        return attrs
    class Meta:
        model = Comment
        fields = '__all__' 
