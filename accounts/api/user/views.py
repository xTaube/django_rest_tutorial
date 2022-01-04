from .serializer import UserDetailSerializer
from django.contrib.auth import get_user_model, authenticate
from rest_framework import generics, pagination
from accounts.api.permissions import AnonPermissionOnly
from status.models import Status
from status.api.serializers import StatusInlineUserSerializer
from restconf.pagination import CFEAPIPagintaion

User = get_user_model()


class UserDetailApiView(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

    def get_serializer_context(self):
        return {'request': self.request}


class UserStatusAPIView(generics.ListAPIView):
    serializer_class = StatusInlineUserSerializer
    # pagination_class = CFEAPIPagintaion
    lookup_field = 'username'

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username", None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)
