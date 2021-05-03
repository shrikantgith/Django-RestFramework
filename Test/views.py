from django.shortcuts import render
from .serializers import MagazineSerializer
from .serializers import ArticleSerializer
from .serializers import AuthorSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Magazine
from .models import Article
from .models import Author
# Create your views here.
# Created Article model viewset
class ArticleViewSet(viewsets.ModelViewSet):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
# Created Magazine model viewset
class MagazineViewSet(viewsets.ModelViewSet):
    queryset=Magazine.objects.all()
    serializer_class=MagazineSerializer
# Created Author model viewset
class AuthorViewSet(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
# Created Custome apiview for Listing authors articles (with Author pk)
class AuthorsArticles_API(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            a=Article.objects.filter(author=id)
            serializer=ArticleSerializer(a,many=True)
            return Response(serializer.data)
        else:
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
# Creating Custome apiview for Getting Article with magazine pk
class ArticlesinMagazine_API(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            a=Article.objects.filter(magazine=id)
            serializer=ArticleSerializer(a,many=True)
            return Response(serializer.data)
        else:
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
