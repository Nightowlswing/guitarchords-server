from api.models import Article, Song, Compositor
from django.contrib.auth.models import User
from api.serializer import SongSerializer, UserSerializer, ArticleSerializer, CompositorSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SongView(APIView):
    def get(self, request, pk, format=None):
        try:
            song = Song.objects.get(pk = pk)
            serializer = SongSerializer(song)
            return Response(serializer.data)
        except Song.DoesNotExist:
            raise Http404

class SongsView(APIView):
    def get(self, request,format=None):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
        
class AddSongView(APIView):
    
    def post(self, request, format = None):
        
        compositor_name = request.data['cname']
        
        if len(Compositor.objects.filter(name = compositor_name)) == 0:
            song_compositor = Compositor(name = compositor_name)
            song_compositor.save()
        song_compositor = Compositor.objects.filter(name = compositor_name)[0]
        # song = Song(
        #     name = request.data['sname'],
        #     compositor = song_compositor,
        #     genre = request.data['genre'],
        #     capo = request.data['capo'],
        #     text = request.data['text']
        # )
        
        serializer = SongSerializer(data = {
            'name': request.data['sname'],
            'compositor': song_compositor.pk,
            'genre': request.data['genre'],
            'capo': request.data['capo'],
            'text': request.data['text']
        } )
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data = serializer.data)
        print(serializer.errors)
        return Response(status=status.HTTP_404_NOT_FOUND)

class CompositorView(APIView):
    def get(self, request,format=None):
        compositors = Compositor.objects.all()
        serializer = CompositorSerializer(compositors, many=True)
        return Response(serializer.data)

class SongsCompView(APIView):
    def get(self,request, pk, format=None):
        compositor = Compositor.objects.get(pk = pk)
        songs = Song.objects.filter(compositor = compositor)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

class ArticlesView(APIView):
    def get(self, request,format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

class SingleArticleView(APIView):
    def get(self, request, pk, format=None):
        try:
            print('get')
            article = Article.objects.get(pk = pk)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        except Song.DoesNotExist:
            raise Http404


class AddArticleView(APIView):
    def post(self, request, format=None):
        print('add')
        article_name = request.data['name']
        if len(Article.objects.filter(name = article_name)) > 0:
            return Response(status=status.HTTP_409_CONFLICT)
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data = serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class SongSearchView(APIView):
    def get(self, request, query, format = None):
        songs = Song.objects.filter(name__contains = query)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

class CompositorSearchView(APIView):
    def get(self, request, query, format = None):
        
        compositors = Compositor.objects.filter(name__contains = query)
        serializer = CompositorSerializer(compositors, many=True)
        return Response(serializer.data)

class ArticleSearchView(APIView):
    def get(self, request, query, format = None):
        article = Article.objects.filter(name__contains = query)
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

