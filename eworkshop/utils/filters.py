from rest_framework.filters import OrderingFilter


class MyOrderingFilter(OrderingFilter):

    ordering = 'created'

    def get_default_ordering(self, view):
        ordering = getattr(view, 'ordering', self.ordering)
        if isinstance(ordering, str):
            return (ordering,)
        return ordering
