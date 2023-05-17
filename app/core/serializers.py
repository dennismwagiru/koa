from rest_framework import serializers

from core.models import Grid


class GridSerializer(serializers.ModelSerializer):
    """Serializer for grid objects"""

    class Meta:
        model = Grid
        fields = ('id', 'points', 'closest_points',)
        read_only_fields = ('id', 'closest_points',)
