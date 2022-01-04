from rest_framework import pagination


class CFEAPIPagintaion(pagination.PageNumberPagination):
    page_size = 5