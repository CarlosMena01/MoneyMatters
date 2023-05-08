from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import TransactionView

router = routers.DefaultRouter()
router.register(r"transaction", TransactionView, "transaction")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title='Transaction API')),
]