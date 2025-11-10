from rest_framework.views import APIView
from rest_framework.response import Response
from agriinfo.models import Crop, Fish, Livestock
from django.db.models import Q

class AgriQuery(APIView):
    def get(self, request):
        name = request.query_params.get("name", "").lower()

        crop = Crop.objects.filter(Q(chichewa__iexact=name) | Q(english__iexact=name) | Q(scientific__iexact=name)).first()
        if crop:
            return Response({"type": "crop", "chichewa": crop.chichewa, "english": crop.english, "scientific": crop.scientific})

        fish = Fish.objects.filter(Q(chichewa__iexact=name) | Q(english__iexact=name) | Q(scientific__iexact=name)).first()
        if fish:
            return Response({"type": "fish", "chichewa": fish.chichewa, "english": fish.english, "scientific": fish.scientific})
        
        livestock = Livestock.objects.filter(Q(chichewa__iexact=name) | Q(english__iexact=name) | Q(scientific__iexact=name)).first()
        if livestock:
            return Response({"type": "livestock", "chichewa": livestock.chichewa, "english": livestock.english, "scientific": livestock.scientific})
        


        return Response({"error": "Not found"}, status=404)
  