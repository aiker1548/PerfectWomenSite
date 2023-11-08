from django.shortcuts import render, get_object_or_404, redirect
from django.http import request, HttpResponse
from women.models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.views.generic.edit import FormView



class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return context|c_def

    def get_queryset(self):
        return Women.objects.filter(is_published=True).select_related('cat')


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title=f'Категория - {cat.name}', cat_selected=cat.pk)
        return context|c_def

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

s = {'asdasda':231, 'adsasd':51234}



class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return context|c_def


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/add_page.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return context|c_def

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return context|c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm #LoginUserForm Ебать ты форму не дописал
    template_name = 'women/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Вход')
        return context|c_def

    def get_success_url(self):
        return reverse_lazy('home')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'women/contaсt.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return context|c_def

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')

def userLogout(request):
    logout(request)
    return redirect('login')

# def about(request):
#     womens = Women.objects.all()
#     paginator = Paginator(womens,5)
#     page_num = request.GET.get('page')
#     page_obj = paginator.get_page(page_num)
#
#     context = {'page_obj': page_obj, 'title': 'Контакты'}
#
#     return render(request, 'women/about.html', context=context)

class About(DataMixin,ListView):
    model = Women
    template_name = 'women/about.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="О странице")
        return context|c_def


#
# def login(request):
#     context = {'menu': menu}
#     return render(request, 'women/login.html', context=context)
#


#
# def addPage_1(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)
#             try:
#                 # Women.objects.create(**form.cleaned_data) сохранение данных через форму, которая не связана с моделью
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления поста')
#     else:
#         form = AddPostForm()
#
#     context = {
#         'form': form,
#         'menu': menu,
#         'title': 'Добавление статьи'
#     }
#     return render(request, 'women/add_page.html', context=context)
#
# def showPost_1(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#     context = {
#         'menu': menu,
#         'post': post,
#         'title': post.title,
#         'cat_selected': post.cat_id
#     }
#
#
#     return render(request, 'women/post.html', context=context)
#
#
# def index_1(request):
#     posts = Women.objects.all()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0
#     }
#     return render(request, 'women/index.html', context=context)
#
# def showCategory_1(request, cat_slug):
#     categoty = get_object_or_404(Category, slug=cat_slug)
#     posts = Women.objects.filter(cat_id=categoty.pk)
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Категории',
#         'cat_selected': categoty.pk
#     }
#     #return render(request, 'women/add_page.html', context=context)
#     return render(request, 'women/index.html', context=context)

