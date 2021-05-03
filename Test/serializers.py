from rest_framework import serializers
from . models import Magazine
from . models import Author
from . models import Article
# Created Model MagazineSerializer
class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Magazine
        fields=['id','Magazine_name']
# Created Model Articleserializer
class ArticleSerializer(serializers.ModelSerializer):
# Displaying the Author name  instead of id
    author=serializers.StringRelatedField(read_only=True)
# Displaying the Magazine name instead of id
    magazine=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=Article
        fields=['id','Headline','Pub_date','author','magazine']
# Created Model AuthorSerializer
class AuthorSerializer(serializers.ModelSerializer):
# Displaying the Article all details using nested serializers instead of just id
    article=ArticleSerializer(many=True,read_only=True)
    class Meta:
        model=Author
        fields=['id','Email','Name','City','article']
