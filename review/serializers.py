from rest_framework import serializers
from review.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["book", "rating", "review_text"]


class ReviewSerializerLong(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
