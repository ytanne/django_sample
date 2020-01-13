from django.urls import path, re_path

from . import views

urlpatterns = [
    path('cars/', views.create_or_list, name="create_or_list"),
    re_path('cars/(?P<car_id>[\d]+)/', views.manipulate_by_id, name="manipulate_by_id"),
]


