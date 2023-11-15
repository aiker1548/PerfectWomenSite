from django.shortcuts import redirect
from women.models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.views.generic.edit import FormView
from datetime import datetime

class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return context | c_def

    def get_queryset(self):
        return Women.objects.filter(is_published=True).select_related('cat')


class ShowUserPosts(DataMixin, ListView):
    model = Women
    template_name = 'women/myPosts.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return context | c_def

    def get_queryset(self):
        return Women.objects.filter(user_id=self.request.user.pk).select_related('cat')


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title=f'Категория - {cat.name}', cat_selected=cat.pk)
        return context | c_def

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')



class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return context | c_def


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/add_page.html'
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return context | c_def

    def form_valid(self, form):
        w = form.save()
        w.user = self.request.user
        w.save()
        return redirect('post', post_slug=w.slug)


class PostUpdateView(LoginRequiredMixin, DataMixin, UpdateView):
    model = Women
    form_class = PostUpdateForm
    template_name = 'women/updatePage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')
    slug_url_kwarg = 'post_slug'

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.user_id != self.request.user.pk:
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Редактирование статьи')
        return context | c_def

    def form_valid(self, form):
        w = form.save()
        w.user = self.request.user
        w.time_update = datetime.now()
        w.save()
        return redirect('post', post_slug=w.slug)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm  # LoginUserForm Ебать ты форму не дописал
    template_name = 'women/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Вход')
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'women/contaсt.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return context | c_def

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


def userLogout(request):
    logout(request)
    return redirect('login')


class About(DataMixin, ListView):
    model = Women
    template_name = 'women/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="О странице")
        return context | c_def

