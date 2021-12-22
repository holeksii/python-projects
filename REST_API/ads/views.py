from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from ads.serializers import AdvertismentDetailSerializer, AdvertismentListSerializer
from ads.models import Advertisment
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .services import PaginationAdvertisments, ReadOnlyOrAdmin


class AdvertismentView(generics.CreateAPIView, generics.ListAPIView):
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = [
        'id',
        'transaction_number',
        'website_url',
        'photo_url',
        'start_date',
        'end_date',
        'title',
        'price',
    ]
    ordering_fields = '__all__'

    def get_queryset(self):
        return Advertisment.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated(), ReadOnlyOrAdmin()]
        elif self.request.method == 'POST':
            return (
                IsAuthenticated(),
                IsAdminUser(),
            )

    serializer_class = AdvertismentListSerializer
    pagination_class = PaginationAdvertisments


class AdvertismentDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get_permissions(self):
        if self.request.method == 'GET' or self.request.method == 'PUT' or self.request.method == 'DELETE':
            return (
                IsAuthenticated(),
                IsAdminUser(),
            )

    serializer_class = AdvertismentDetailSerializer
    queryset = Advertisment.objects.all()
