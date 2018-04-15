from api.models import Expert
from rest_framework import viewsets
from api.serializers import ExpertSerializer


class ExpertViewSet(viewsets.ModelViewSet):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer
