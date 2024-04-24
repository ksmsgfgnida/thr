
from .models import Category, Performance
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from .models import Profile

from .forms import UserRegisterForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView

from .forms import UserLoginForm
from .forms import PerformanceForm


class UserRegisterView(SuccessMessageMixin, CreateView):
    """
    Представление регистрации на сайте с формой регистрации
    """
    form_class = UserRegisterForm
    success_url = reverse_lazy('profile')
    template_name = 'register.html'
    success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context


class UserLoginView(SuccessMessageMixin, LoginView):
    """
    Авторизация на сайте
    """
    form_class = UserLoginForm
    template_name = 'login.html'
    next_page = 'profile'
    success_message = 'Добро пожаловать на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context



def profile(request, user):
    profile = Profile.get.object(username=user)
    return render(request, 'profile.html', {'profile': profile})


def category_performance_list(request, category_id):
    category = Category.objects.get(name=category_id)
    performances = Performance.objects.filter(category=category)
    return render(request, 'category_performance_list.html', {'category': category, 'performances': performances})


def performance_list(request):
    performances = Performance.objects.all()
    return render(request, 'performance_list.html', {'performances': performances})

def performance_detail(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    return render(request, 'performance_detail.html', {'performance': performance})

def performance_create(request):
    if request.method == 'POST':
        form = PerformanceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('performance_list')
    else:
        form = PerformanceForm()
    return render(request, 'performance_create.html', {'form': form})

def performance_update(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    if request.method == 'POST':
        form = PerformanceForm(request.POST, request.FILES, instance=performance)
        if form.is_valid():
            form.save()
            return redirect('performance_detail', pk=performance.pk)
    else:
        form = PerformanceForm(instance=performance)
    return render(request, 'performance_update.html', {'form': form, 'performance': performance})



def performance_delete(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    if request.method == 'POST':  # Only delete on POST
        performance.delete()
        return redirect('performance_list')
    return render(request, 'performance_delete.html', {'performance': performance})



def index(request):
    return render(request, 'index.html')



# Create your views here.
