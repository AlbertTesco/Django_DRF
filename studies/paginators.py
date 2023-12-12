from rest_framework.pagination import PageNumberPagination


class StudiesPaginator(PageNumberPagination):
    """
    Класс для постраничного вывода информации
    """
    page_size = 5
