from django.contrib.auth.models import Group

from rest_framework import viewsets, mixins

from ..serializers import GroupSerializer


class GroupViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filterset_fields = ['created', 'modified', ]
