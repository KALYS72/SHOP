from rest_framework.serializers import ModelSerializer
from .models import Comment, Rate


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('author',)

    def validate(self, attrs):
        attrs =  super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        del rep['product']
        rep['author'] = instance.author.email
        return rep


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rate
        exclude = ('author',)

    def validate(self, attrs):
        attrs =  super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs