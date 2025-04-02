from django.urls import path
from . import views


urlpatterns = [
    path('', views.bureau, name='bureau'),
    path('chambre', views.chambre, name='chambre'),
    path('salon', views.salon, name='salon'),
    path('description/', views.description, name='description'),
    



]


