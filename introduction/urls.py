from django.urls import path
from introduction.views import index, analysis, device, about, service

urlpatterns = [
    path('', index, name='index'),
    path('analysis', analysis, name='analysis'),
    path('device', device, name='device'),
    path('about', about, name='about'),
    path('service', service, name='service'),
]
