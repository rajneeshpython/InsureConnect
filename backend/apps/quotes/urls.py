# apps/quotes/urls.py
from rest_framework.routers import DefaultRouter
from .views import QuoteRequestViewSet, QuoteViewSet

router = DefaultRouter()
router.register(r"requests", QuoteRequestViewSet, basename="quote-request")
router.register(r"quotes", QuoteViewSet, basename="quote")

urlpatterns = router.urls
