from django.http import JsonResponse
from rest_framework.views import APIView
from celeryapp import tasks


class ScraperAPIView(APIView):
    def get(self, request):
        tasks.start_scraper.delay()
        return JsonResponse({"scraper_started": True})
