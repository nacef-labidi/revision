"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from posts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # ListView des posts en homepage
    url(r'^$', views.PostList.as_view(), name='post_list'),

    # Utilise la meme ListView pour la homepage mais lui passe le category_id pour filtrer les posts par categorie
    url(r'^posts/category/(?P<category_id>\d+)/$', views.PostList.as_view(), name='post_category'),

    # CreateView pour la creation de posts
    url(r'^posts/create$', views.PostCreate.as_view(), name='post_create'),

    # DetailView page de detail d'un post
    url(r'^post/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='post_detail'),

    # URLs necessaires pour le login
    url(r'^accounts/', include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Necessaire pour pouvoir afficher les images sur le site
