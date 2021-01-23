from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from collections import OrderedDict


class MyPagination(LimitOffsetPagination):

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.count),
            ('limit', self.limit),
            ('offset', self.offset),
            ('results', data)
        ]))
