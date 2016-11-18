from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin   # Necessaire pour activer le login sur la CreateView

from models import Post, Category


class PostList(ListView):
    model = Post
    context_object_name = 'posts'   # Renommage du nom de la variable de contexte de la view

    # Override de la recuperation de contexte pour y ajouter la liste des categories a afficher sur la homepage
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    # Redefinition du get_queryset pour effectuer un filtrage de la liste des posts par category_id
    def get_queryset(self):
        category_id = self.kwargs.get('category_id', None)
        if category_id:
            return Post.objects.filter(categories=category_id)

        return super(PostList, self).get_queryset()


# View de creation de post
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = '__all__'      # On doit specifier les champs du form, ici on a pris tous les champs
    success_url = '/'       # URL vers laquelle on redirige apres le succes de l'ajout


class PostDetail(DetailView):
    model = Post