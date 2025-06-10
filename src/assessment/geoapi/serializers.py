from rest_framework import serializers
from django.contrib.gis.geos import Point
from .models import GeoLocation

class GeoLocationSerializer(serializers.ModelSerializer):
    # lat, long fields en andere fields read-only maken, geen directe set
    latitude = serializers.FloatField(write_only=True)
    longitude = serializers.FloatField(write_only=True)

    class Meta:
        model = GeoLocation
        fields = ['id', 'location', 'timestamp', 'user', 'latitude', 'longitude']
        extra_kwargs = {
            'location': {'read_only': True},
            'user': {'read_only': True},
            'timestamp': {'read_only': True}
        }

    def create(self, validated_data):
        latitude = validated_data.pop('latitude')
        longitude = validated_data.pop('longitude')

        point = Point(longitude, latitude)

        validated_data['location'] = point

        return super().create(validated_data)


