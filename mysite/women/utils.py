from .models import *
from django.db.models import Count
from django.core.cache import cache

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Контакты", 'url_name': 'contact', 'UserIn': 0}
]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats_with_posts = cache.get('cats')
        if not cats_with_posts:
            cats_with_posts = Category.objects.annotate(women_count=Count('women')).filter(women_count__gt=0)
            cache.set('cats', cats_with_posts, 60)

        user_menu = menu.copy()

        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats_with_posts
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

    # def validButtonsPages(self, **kwargs):
    #     if context['paginator'].num_pages > 1:
    #         if context[]


