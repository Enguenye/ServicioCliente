
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Courses
from .models import Cajas
from .models import Productos

class CourseList(ListView):
    model = Courses


class CourseDetail(DetailView):
    model = Courses


class CourseCreation(CreateView):
    model = Courses
    success_url = reverse_lazy('courses:list')
    fields = ['fecha', 'cantidad','tipo']


class CourseUpdate(UpdateView):
    model = Courses
    success_url = reverse_lazy('courses:list')
    fields = ['fecha', 'cantidad', 'tipo']


class CourseDelete(DeleteView):
    model = Courses
    success_url = reverse_lazy('courses:list')


class CajaList(ListView):
    model = Cajas


class CajaDetail(DetailView):
    model = Cajas


class CajaCreation(CreateView):
    model = Cajas
    success_url = reverse_lazy('courses:list')
    fields = ['identificador', 'certificada']


class CajaUpdate(UpdateView):
    model = Cajas
    success_url = reverse_lazy('courses:list')
    fields = ['identificador', 'certificada']


class CajaDelete(DeleteView):
    model = Cajas
    success_url = reverse_lazy('courses:list')


class ProductoList(ListView):
    model = Productos


class ProductoDetail(DetailView):
    model = Productos


class ProductoCreation(CreateView):
    model = Productos
    success_url = reverse_lazy('courses:list')
    fields = ['identificador', 'precio','cantidad']


class ProductoUpdate(UpdateView):
    model = Productos
    success_url = reverse_lazy('courses:list')
    fields = ['identificador', 'precio', 'cantidad']


class ProductoDelete(DeleteView):
    model = Productos
    success_url = reverse_lazy('courses:list')
