from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateField(auto_now_add=True)  # auto_now_add=True assigne la valeur du champs pub_date juste a la creation d'un post
    last_modified = models.DateField(auto_now=True) # auto_now=True assigne la valeur du champ last_modified a chaque sauvegarde du post
    photo = models.ImageField(upload_to='photos')   # Le parametre upload_to designe le dossier sur le disque dans lequel seront sauvegardees les images uploadees par ce champs
    tags = models.CharField(max_length=255)
    author = models.ForeignKey(Author)
    categories = models.ManyToManyField(Category)   # On definit le champ ManyToManyField d'un seul coté de la relation

    class Meta:                         # La classe Meta permet de passer des parametres de configuration au niveau de la classe
        ordering = ['-pub_date']        # Dans notre cas on a défini l'ordering sur les dates de publications descendantes, sera applique pour toutes les requetes

    def __str__(self):
        return self.title

