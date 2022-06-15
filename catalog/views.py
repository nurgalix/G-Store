from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Catalog


class ViewCatalog(ListView):
    model = Catalog
    template_name = 'catalog/view_catalog_list.html'
    context_object_name = 'catalog'
