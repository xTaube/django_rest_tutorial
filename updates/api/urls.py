from django.urls import path, re_path, include
from .views import (
        UpdateModelDetailAPIView,
        UpdateModelListAPIView
    )

urlpatterns = [
    path('', UpdateModelListAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'(?P<id>\d+)/', UpdateModelDetailAPIView.as_view())
]