from django.urls import path
from .views import ConvertToForeign, ConvertToMWK

urlpatterns = [
    path("to_foreign/", ConvertToForeign.as_view()),
    path("to_mwk/", ConvertToMWK.as_view()),
]
