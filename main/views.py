
from .models import Category, Performance, User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login


from .forms import RegistrationForm, LoginForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView

from .forms import PerformanceForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})



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
