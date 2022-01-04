from rest_framework import serializers
from status.models import Status
from accounts.api.serializers import UserPublicSerializer
from rest_framework.reverse import reverse as api_reverse

# class CustomSerializer(serializers.Serializer):
#     content = serializers.CharField()
#     email =  serializers.EmailField()


class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    # user = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    # user = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
    user_id = serializers.HyperlinkedRelatedField(source='user', lookup_field='username', view_name='api-user:detail', read_only=True)
    username = serializers.SlugRelatedField(read_only=True, source='user', slug_field='username')
    class Meta:
        model = Status
        fields = [
            "uri",
            "user_id",
            "id",
            "user",
            "content",
            'username',
            "image"
        ]

        read_only_fields = ['user']

    # def get_user(self, obj):
    #     request = self.context.get('request')
    #     user = obj.user
    #     return UserPublicSerializer(user, read_only=True, context={'request': request}).data

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse("api-status:detail", kwargs={'id': obj.id}, request=request)

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None

        image = data.get("image", None)

        if content is None and image is None:
            raise serializers.ValidationError("Content or image needed")

        return data


class StatusInlineUserSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Status
        fields = [
            'uri',
            'id',
            'content',
            'image'
        ]

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse("api-status:detail", kwargs={'id': obj.id}, request=request)