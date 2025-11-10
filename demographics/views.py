from rest_framework.views import APIView
from rest_framework.response import Response
from demographics.models import Demographics

class DemographicsList(APIView):   
    def get(self, request):   
        demographics = Demographics.objects.all().values_list("name", flat=True)
        return Response(list(demographics))

class DemographicsDetail(APIView):
    def get(self, request, name):       
        try:  
            demodetails = Demographics.objects.get(name__iexact=name)
            data = {
                "name": demodetails.name,
                "region": demodetails.region,
                "population": demodetails.population,
                "urban_percent": demodetails.urban_percent
            }
            return Response(data)
        except Demographics.DoesNotExist:
            return Response({"error": "Demographics not found"}, status=404)
  