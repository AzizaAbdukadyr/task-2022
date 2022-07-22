from rest_framework import viewsets, generics
from task1.models import Zadacha
from django.views import generic
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView



class ZadachaCreate(CreateView):
    model = Zadacha
    template_name = "task_create.html"
    fields = "__all__"
    success_url = "/task_list"


class ZadachaListView(ListView):
    model = Zadacha
    template_name = "task_list.html"
    def get_queryset(self):
        qs = Zadacha.objects.all()
        return qs


class ZadachaDetails(DetailView):
    model = Zadacha
    template_name = "task_detail.html"


class ZadachaUpdate(UpdateView):
    model = Zadacha
    template_name = "task_create.html"
    fields = "__all__"
    success_url = "/task_list"


class ZadachaDelete(DeleteView):
    model = Zadacha
    template_name = "task_delete.html"
    success_url = "/task_list"
