
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
# from rest_framework.authtoken import views as token_view

urlpatterns = [
    path('song/<int:pk>', views.SongView.as_view()),
    path('allSongs/', views.SongsView.as_view()),
    path('addSong/', views.AddSongView.as_view()),

    path('allComp/', views.CompositorView.as_view()),
    path('allSongsOfC/<int:pk>', views.SongsCompView.as_view()),

    path('article/<int:pk>', views.SingleArticleView.as_view()),
    path('ArticlesView/', views.ArticlesView.as_view()),
    path('addArticle/', views.AddArticleView.as_view()),

    path('searchS/<str:query>', views.SongSearchView.as_view()),
    path('searchA/<str:query>', views.ArticleSearchView.as_view()),
    path('searchC/<str:query>', views.CompositorSearchView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)