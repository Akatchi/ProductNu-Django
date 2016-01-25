from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from django.http import JsonResponse
from requests import Response
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
from rest_framework.decorators import api_view
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.views import APIView

from celeryapp import tasks

from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

#@api_view(['GET', 'POST'])
#def start_scraper():
    #tasks.start_scraper.delay()  # Should do the trick

class ScraperAPIView(APIView):
    def get(self, request):
        tasks.start_scraper.delay()
        return JsonResponse({"hanzestatus": "7/7"})


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'scraper', ScraperAPIView.as_view(), base_name=ScraperAPIView)

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'main.views.home', name='home'),
#     # url(r'^blog/', inclu/de('blog.urls')),
#     url(r'^', include(router.urls)),
#
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [
    url(r'^scraper/$', ScraperAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
