"""API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from Test import views
from rest_framework.routers import DefaultRouter
# Creating Router Object
router=DefaultRouter()
# Registering Article
router.register('articles',views.ArticleViewSet,basename='article')
# Registering Magazine
router.register('magazines',views.MagazineViewSet,basename='magazine')
# Registering Author
router.register('authors',views.AuthorViewSet,basename='author')
# # Registering Custome GET (get all articles related to author with pk)
# router.register('authors/<int:pk>/articles',views.AuthorsarticleViewSet,basename='authorsarticle')

urlpatterns = [
    path("",include(router.urls)),
    path('authors/<int:pk>/articles',views.AuthorsArticles_API.as_view()),
    path('magazines/<int:pk>/articles',views.ArticlesinMagazine_API.as_view())    
]
