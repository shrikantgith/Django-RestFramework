from django.db import models

# Create your models here.
# Magazine Model
class Magazine(models.Model):
    Magazine_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Magazine_name
# Author Model
class Author(models.Model):
    Email=models.EmailField(max_length=50)
    Name=models.CharField(max_length=50)
    City=models.CharField(max_length=20)

    def __str__(self):
        return self.Name
# Article Model
class Article(models.Model):
    Headline=models.CharField(max_length=100)
    Pub_date=models.DateField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='article')
    magazine=models.ManyToManyField(Magazine,related_name='magazine')

    def __self__(self):
        return self.Headline

