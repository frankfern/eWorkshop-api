from django.core.exceptions import FieldError
from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet
from django.utils.datastructures import MultiValueDictKeyError


class DynamicOrderingDecorator():
    def __call__(self, cls):
        class Wrapped(cls):

            """
            docstring
            """

            def get_queryset(self):
                """
                Return the list of items for this view.

                The return value must be an iterable and may be an instance of
                `QuerySet` in which case `QuerySet` specific behavior will be enabled.
                """
                if self.queryset is not None:
                    queryset = self.queryset
                    if isinstance(queryset, QuerySet):
                        queryset = queryset.all()
                elif self.model is not None:
                    queryset = self.model._default_manager.all()
                else:
                    raise ImproperlyConfigured(
                        "%(cls)s is missing a QuerySet. Define "
                        "%(cls)s.model, %(cls)s.queryset, or override "
                        "%(cls)s.get_queryset()." % {
                            'cls': self.__class__.__name__
                        }
                    )

                try:
                    ordering = self.get_ordering()
                    dandi = self.finallyorder(ordering, queryset)
                except FieldError as tiza:
                    ordering = ('-id',)
                    dandi = self.finallyorder(ordering, queryset)

                return dandi

            def get_ordering(self):
                return self.request.GET.get(
                    'order', '-id').split(',')

            def finallyorder(self, ordering, queryset):

                if ordering:
                    if isinstance(ordering, str):
                        ordering = (ordering,)
                    queryset = queryset.order_by(*ordering)

                return queryset

        return Wrapped


class DynamicPaginateBy():
    """
    docstring
    """

    def __call__(self, cls):
        class Wrapper(cls):
            def get_paginate_by(self, queryset):

                limit = self.request.GET.get('limit', 7)

                try:
                    limit = int(limit)
                    self.paginate_by = limit

                except ValueError:
                    self.paginate_by = 10

                finally:
                    return self.paginate_by
        return Wrapper


class GetToPostDecorator():
    def __call__(self, cls):
        class Wrapped(cls):
            def get(self, request, *args, **kwargs):
                return self.post(request, *args, **kwargs)

        return Wrapped
