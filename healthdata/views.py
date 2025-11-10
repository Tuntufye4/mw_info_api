from rest_framework.views import APIView
from rest_framework.response import Response
from healthdata.models import Healthdata

class HealthdataList(APIView):   
    def get(self, request):   
        healthdata = Healthdata.objects.all().values_list("name", flat=True)
        return Response(list(healthdata))

class HealthDetail(APIView):  
    def get(self, request, name):    
        try:
            healthdetails = Healthdata.objects.get(name__iexact=name)
            data = {
                "name":healthdetails.name,
                "region": healthdetails.region,
                "health_centers": healthdetails.health_centers,
                "hospitals": healthdetails.hospitals,  
                "dispensaries": healthdetails.dispensaries,
            }
            return Response(data)  
        except Healthdata.DoesNotExist:
            return Response({"error": "Health data not found"}, status=404)
  