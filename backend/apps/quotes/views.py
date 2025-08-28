# apps/quotes/views.py
from rest_framework import viewsets, permissions
from .models import QuoteRequest, Quote
from .serializers import QuoteRequestSerializer, QuoteSerializer

class QuoteRequestViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return QuoteRequest.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        quote_request_id = self.request.query_params.get("quote_request")
        if quote_request_id:
            queryset = queryset.filter(quote_request_id=quote_request_id)
        return queryset


