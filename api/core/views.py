from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, mixins
from api.core.serializers import UserSerializer, GroupSerializer

class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,  mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
