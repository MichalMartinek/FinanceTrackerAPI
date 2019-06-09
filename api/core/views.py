from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import views, viewsets, mixins
from rest_framework.response import Response
from api.core.serializers import UserSerializer, GroupSerializer

class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,  mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class SearchUserView(views.APIView):
    def get(self, request, query):
        print(query)
        queryset = User.objects.exclude(id=request.user.id).filter(Q(username__icontains=query) | Q(email__icontains=query)).all()
        serializer = UserSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)