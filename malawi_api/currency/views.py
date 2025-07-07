from rest_framework.views import APIView
from rest_framework.response import Response
from currency.models import CurrencyRate

class ConvertToForeign(APIView):
    def get(self, request):
        amount = float(request.query_params.get("amount", 0))
        code = request.query_params.get("currency", "").upper()

        try:
            rate = CurrencyRate.objects.get(code=code)
            return Response({
                "mwk": amount,
                "currency": code,
                "converted": round(amount / rate.rate_to_mwk, 2)
            })
        except CurrencyRate.DoesNotExist:
            return Response({"error": "Currency not supported"}, status=404)

class ConvertToMWK(APIView):
    def get(self, request):
        amount = float(request.query_params.get("amount", 0))
        code = request.query_params.get("currency", "").upper()

        try:
            rate = CurrencyRate.objects.get(code=code)
            return Response({
                "currency": code,
                "foreign": amount,
                "converted": round(amount * rate.rate_to_mwk, 2)
            })
        except CurrencyRate.DoesNotExist:
            return Response({"error": "Currency not supported"}, status=404)
