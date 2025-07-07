from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include

def home(request):
    return JsonResponse({
        "message": "MW INFO API",
        "available_endpoints": [
            "/api/mwinfo/",
            "/api/agriinfo/",
            "/api/currency/",
        ]
    })

urlpatterns = [
    path('', home),  # 👈 Root route
    path('admin/', admin.site.urls),
    path('api/mwinfo/', include('mwinfo.urls')),
    path('api/agriinfo/', include('agriinfo.urls')),
    path('api/currency/', include('currency.urls')),
]
