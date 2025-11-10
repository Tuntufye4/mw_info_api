from django.urls import path
from .views import DistrictList, DistrictDetail

urlpatterns = [
    path("districts/", DistrictList.as_view()),
    path("districts/<str:name>/", DistrictDetail.as_view()),
]
   