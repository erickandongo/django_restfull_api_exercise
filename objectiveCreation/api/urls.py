from django.urls import path 
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.objectives, name="all-objectives"),
    path('objective_details/<str:pk>/', views.objective_details, name="objective-details"),
    path('create_objective/', views.objective_creation, name="create-objective")
]
