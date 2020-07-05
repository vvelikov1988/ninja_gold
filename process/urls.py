from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('process_money', views.process),
    path('farm_action', views.farm_action),
    path('cave_action', views.cave_action),
    path('house_action', views.house_action),
    path('casino_action', views.casino_action),
]