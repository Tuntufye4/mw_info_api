from django.urls import path
from .views import HealthdataList, HealthDetail

urlpatterns = [
    path("healthdata/", HealthdataList.as_view()),
    path("healthdata/<str:district>/", HealthDetail.as_view()),
]
