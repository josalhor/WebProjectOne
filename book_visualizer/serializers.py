from .models import Comment, Book
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

class GetWishSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ('isbn', 'title', 'author', 'date', 'bestsellers_date', 'publisher', 'summary')

class PostWishSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        user = self.context['request'].user
        book = Book.objects.all().filter(isbn=validated_data['isbn']).first()
        book.wished_by.add(user)
        return book

    def destroy(self, request, *args, **kwargs):
        from rest_framework.response import Response
        from rest_framework import status
        print(request)
        instance = self.get_object()
        print(instance)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    class Meta:
        model = Book
        fields = ('isbn',)
