from rest_framework import serializers

from .models import BlogModel


class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
    title = serializers.CharField(required=True, allow_blank=True, max_length=100)
    details = serializers.CharField(max_length=1200, )
    user = serializers.CharField(max_length=50)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return BlogModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
