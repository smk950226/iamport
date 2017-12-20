from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ItemListView.as_view(), name='index'),
]