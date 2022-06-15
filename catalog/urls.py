from django.urls import path

from catalog import views

urlpatterns = [
    path('', views.ViewCatalog.as_view(), name='catalog')
]
