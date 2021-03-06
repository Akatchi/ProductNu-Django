from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import ScraperAPIView


urlpatterns = [
    url(r'^scraper/$', ScraperAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
