from rest_framework import serializers


class FruitSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
