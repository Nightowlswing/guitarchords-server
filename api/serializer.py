from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Song, Article, Compositor
    
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','name', 'compositor', 'genre', 'capo', 'text']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'name', 'text']

class CompositorSerializer(serializers.ModelSerializer):
    songs = serializers.PrimaryKeyRelatedField(many=True, queryset=Song.objects.all())
    class Meta:
        model = Compositor
        fields = ['id', 'username', 'songs']   

