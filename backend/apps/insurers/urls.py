from django.urls import path
from .views import InsurerListView, InsurancePlanListView

urlpatterns = [
    path("insurers/", InsurerListView.as_view(), name="insurer_list"),
    path("plans/", InsurancePlanListView.as_view(), name="plan_list"),
]
