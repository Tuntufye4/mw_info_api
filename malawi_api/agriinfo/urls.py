from django.urls import path
from .views import CropFishQuery

urlpatterns = [
    path("query/", CropFishQuery.as_view()),
]
