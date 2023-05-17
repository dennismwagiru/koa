from rest_framework import viewsets, mixins

from core.models import Grid
from core import serializers


class GridViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin):
    """Manage grids in the database"""
    queryset = Grid.objects.all()
    serializer_class = serializers.GridSerializer
