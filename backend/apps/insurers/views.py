from rest_framework import generics
from .models import Insurer, InsurancePlan
from .serializers import InsurerSerializer, InsurancePlanSerializer

# List all insurers
class InsurerListView(generics.ListAPIView):
    queryset = Insurer.objects.all()
    serializer_class = InsurerSerializer


# List plans for a specific insurer or all plans
class InsurancePlanListView(generics.ListAPIView):
    queryset = InsurancePlan.objects.all()
    serializer_class = InsurancePlanSerializer
