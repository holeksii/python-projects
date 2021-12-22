from django.urls import path
from ads.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Advertismet",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@jewelry.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

app_name = 'adv'

urlpatterns = [
    path('adv/', AdvertismentView.as_view()),
    path('adv/<int:pk>/', AdvertismentDetailView.as_view()),
    path('',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
]
