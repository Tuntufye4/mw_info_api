from django.urls import path
from .views import DemographicsList, DemographicsDetail

urlpatterns = [
    path("demographics/", DemographicsList.as_view()),
    path("demographics/<str:name>/", DemographicsDetail.as_view()),
]
