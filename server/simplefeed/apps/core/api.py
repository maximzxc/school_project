from rest_framework.routers import DefaultRouter
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin, RetrieveModelMixin,
    UpdateModelMixin, DestroyModelMixin
)

from core.models import (
    User,
    Message,
)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message


class UserViewSet(
        ListModelMixin,
        RetrieveModelMixin,
        UpdateModelMixin,
        DestroyModelMixin,
        CreateModelMixin,
        GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ["email", ]

    def dispatch(self, request, *args, **kwargs):
        if kwargs.get('pk') == 'current':
            kwargs['pk'] = request.user.pk

        return super(UserViewSet, self).dispatch(request, *args, **kwargs)


class MessageViewSet(
        ListModelMixin,
        RetrieveModelMixin,
        UpdateModelMixin,
        DestroyModelMixin,
        CreateModelMixin,
        GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_fields = ["sender", ]


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'messages', MessageViewSet)
