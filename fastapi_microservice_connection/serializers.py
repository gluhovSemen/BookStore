from rest_framework import serializers


class BaseSalesSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    book_title = serializers.CharField()
    author = serializers.CharField()
    purchase_price = serializers.FloatField()
    purchase_quantity = serializers.IntegerField()


class SalesSchemaDisplaySerializer(BaseSalesSerializer):
    id = serializers.IntegerField()
    created_at = serializers.DateTimeField()


class MostSoldBookSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()


class SoldDaysSerializer(serializers.Serializer):
    day = serializers.CharField()


class MostSoldDaysSerializer(SoldDaysSerializer):
    total_sales = serializers.IntegerField()
