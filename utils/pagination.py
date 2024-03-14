from rest_framework.pagination import PageNumberPagination
from django.http import JsonResponse


class Pagination(PageNumberPagination):

    def __init__(self) -> None:
        super(Pagination, self).__init__()
        self.page_size_query_param = 'size'

    def get_paginated_response(self, data):
        return JsonResponse({
            'count': self.page.paginator.count,
            'size': self.page.paginator.per_page,
            'page': self.page.number,
            'data': data
        })
