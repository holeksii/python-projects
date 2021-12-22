from rest_framework import serializers
from ads.models import Advertisment


class AdvertismentListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError(
                "Start date should be earlier than End date")
        return data

    class Meta:
        model = Advertisment
        fields = '__all__'


class AdvertismentDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError(
                "Start date should be earlier than End date")
        return data

    class Meta:
        model = Advertisment
        fields = '__all__'
