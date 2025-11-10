from rest_framework.views import APIView
from rest_framework.response import Response
from mwinfo.models import District

class DistrictList(APIView):
    def get(self, request):   
        districts = District.objects.all().values_list("name", flat=True)
        return Response(list(districts))

class DistrictDetail(APIView):   
    def get(self, request, name):
        try:
            district = District.objects.get(name__iexact=name)
            data = {
                "name": district.name,
                "region": district.region,
                "latitude": district.latitude,
                "longitude": district.longitude,
                "capital": district.capital,
                "population_2023": district.population_2023,
                "area_km2": district.area_km2,
                "density": district.density,
                "elevation_m": district.elevation_m,
                "climate": district.climate,
                "timezone": district.timezone,
                "languages": district.languages   
            }
            return Response(data)
        except District.DoesNotExist:
            return Response({"error": "District not found"}, status=404)
