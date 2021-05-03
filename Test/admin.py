from django.contrib import admin
from . models import Author
from . models import Article
from . models import Magazine
# Register your models here.
# Using Decorators for registation
# Magazine
@admin.register(Magazine)
class Magazine(admin.ModelAdmin):
    list_display=('id','Magazine_name')
# Author
@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display=('id','Email','Name','City')
# Article
@admin.register(Article)
class Article(admin.ModelAdmin):
    list_display=('id','Headline','Pub_date','author','Magazines')
# Displaying Magazines in  admin.py at Article tabel
    def Magazines(self, obj):
        return "\n".join([p.Magazine_name for p in obj.magazine.all()])



