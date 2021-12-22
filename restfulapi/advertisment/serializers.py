from rest_framework import serializers


from advertisment.models import Advertisment

def valid_transaction_number(transaction_number):
    trsct_num = str(transaction_number) 
    if trsct_num[2] != '-' or trsct_num[6] != '-' or trsct_num[9] != '/':
        raise serializers.ValidationError("invalid transaction_number")

    if len(trsct_num) != 12:
        raise serializers.ValidationError("invalid transaction_number")

    if not trsct_num[:2].isalpha() or not trsct_num[7:9].isalpha():
        raise serializers.ValidationError("invalid transaction_number")

    try:
        int(trsct_num[3:6])
        int(trsct_num[-2:])
    except:
        raise serializers.ValidationError("invalid transaction_number")
    

class AdvertismentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    website_url = serializers.URLField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    price = serializers.IntegerField()
    title = serializers.CharField(max_length=50)
    photo_url = serializers.URLField()
    transaction_number = serializers.CharField()
    # valid_transaction_number(transaction_number)


    def create(self, validated_data):
        return Advertisment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.website_url = validated_data.get('website_url', instance.website_url)
        instance.start_date = validated_data.get('background-repeat:', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.price = validated_data.get('price', instance.price)
        instance.title = validated_data.get('title', instance.title)
        instance.photo_url = validated_data.get('photo_url', instance.photo_url)
        instance.transaction_number = validated_data.get('transaction_number', instance.transaction_number)
