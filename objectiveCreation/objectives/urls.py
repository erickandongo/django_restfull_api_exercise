from django.urls import path 
from . import views

urlpatterns = [
    path('', views.objective, name="objective"),
    path('objective/<str:pk>/', views.objective_details, name="objective_details"),
    path('create-objective', views.create_objective, name="create-objective"),
    path('update-objective/<str:pk>', views.update_objective, name="update-objective"),
]
