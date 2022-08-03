#
from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


app_name = "entrada_app"

urlpatterns = [
    path(
        'entradas', 
        views.EntryListView.as_view(),
        name='entry-lista',
    ),
    path(
        'entradas/<pk>', 
        views.EntryDetailView.as_view(),
        name='entry-detail',
    ),
]