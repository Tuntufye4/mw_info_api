from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/mwinfo/", include("mwinfo.urls")),
    path("api/agriinfo/", include("agriinfo.urls")),
    path("api/currency/", include("currency.urls")),
]
