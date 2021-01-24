from collections import OrderedDict
from base64 import b64encode
from collections import OrderedDict
from urllib import parse

from rest_framework.pagination import CursorPagination
from rest_framework.response import Response


class MyPagination(CursorPagination):
    page_size_query_param = 'limit'

    def encode_cursor(self, cursor):
        """
            Given a Cursor instance, return an url with encoded cursor.
            """
        tokens = {}
        if cursor.offset != 0:
            tokens['o'] = str(cursor.offset)
        if cursor.reverse:
            tokens['r'] = '1'
        if cursor.position is not None:
            tokens['p'] = cursor.position

        querystring = parse.urlencode(tokens, doseq=True)
        encoded = b64encode(querystring.encode('ascii')).decode('ascii')

        return encoded

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('param_name', self.cursor_query_param),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
