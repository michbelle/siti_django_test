from django.urls import path

from . import views
app_name='polls'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/localita/
    path('<int:id>/sito/', views.sito_id, name='sito_id'),
    path('<int:id>/localita/', views.localita, name='localita'),
    path('recenti/', views.recenti, name='recenti'),
    path('<int:id>/detail/', views.detail, name='detail'),
    path('map', views.mapping, name='map'),
]
