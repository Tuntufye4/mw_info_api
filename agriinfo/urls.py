from django.urls import path
from .views import AgriQuery

urlpatterns = [
    path("agriquery/", AgriQuery.as_view()),
]
  