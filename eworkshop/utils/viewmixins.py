class ListCreateSerializerMixin(object):
    """
    Overrides get_serializer_class to choose the read serializer
    for GET requests and the write serializer for POST requests.

    Set read_serializer_class and write_serializer_class attributes on a
    viewset. 
    """
    list_serializer_class = None
    write_serializer_class = None

    def get_serializer_class(self):

        if (self.action == 'list'):
            return self.get_list_serializer_class()

        else:
            return self.get_write_serializer_class()

    def get_list_serializer_class(self):
        assert self.list_serializer_class is not None, (
            "'%s' should either include a `list_serializer_class` attribute,"
            "or override the `get_list_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.list_serializer_class

    def get_write_serializer_class(self):
        assert self.write_serializer_class is not None, (
            "'%s' should either include a `write_serializer_class` attribute,"
            "or override the `get_write_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.write_serializer_class


class RetrieveUpdateAPIView(ListCreateSerializerMixin):

    def get_serializer_class(self):

        if (self.request.method == 'GET'):
            return self.get_list_serializer_class()

        else:
            return self.get_write_serializer_class()
