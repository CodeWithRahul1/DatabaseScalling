from rest_framework import serializers
from app.models import SaleOrder

class SaleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrder
        fields = ['id', 'customer_name', 'amount', 'region']

    def create(self, validated_data):
        # Extract region and save order in the correct shard
        region = validated_data.get('region', 'default_region')

        # Specify the shard to save the order
        return SaleOrder.objects.using(region).create(**validated_data)
