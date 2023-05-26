# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

from fastapi_microservice_connection.serializers import (
    SalesSchemaDisplaySerializer,
    MostSoldBookSerializer,
    MostSoldDaysSerializer,
    SoldDaysSerializer,
)
from fastapi_microservice_connection.servises import HTTPRequest


class BaseSalesAPIView(APIView):
    pagination_class = None
    serializer_class = SalesSchemaDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]


class AllSalesListAPIView(BaseSalesAPIView, ListAPIView):
    def get_queryset(self):
        return HTTPRequest.run("/sales")


class MostExpensiveSaleAPIView(BaseSalesAPIView, RetrieveAPIView):
    def get_object(self):
        return HTTPRequest.run("/sales/most-expensive")


class MostSoldBookByQuantityAPIView(BaseSalesAPIView, RetrieveAPIView):
    serializer_class = MostSoldBookSerializer

    def get_object(self):
        return HTTPRequest.run("/sales/most-sold-book-by-quantity")


class MostSoldBookByPriceAPIView(BaseSalesAPIView, RetrieveAPIView):
    serializer_class = MostSoldBookSerializer

    def get_object(self):
        return HTTPRequest.run("/sales/most-sold-book-by-price")


class SalesByUserListAPIView(BaseSalesAPIView, ListAPIView):
    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return HTTPRequest.run("/sales/user", user_id=user_id)


class SalesByDateListAPIView(BaseSalesAPIView, ListAPIView):
    # @swagger_auto_schema(manual_parameters=[
    #     openapi.Parameter('day', openapi.IN_QUERY, description='The day to filter sales by', type=openapi.TYPE_STRING),
    # ])
    def get_queryset(self):
        day = self.request.query_params.get("day")
        return HTTPRequest.run("/sales/date", day=day)


class MostSoldDaysListAPIView(BaseSalesAPIView, ListAPIView):
    serializer_class = MostSoldDaysSerializer

    def get_queryset(self):
        return HTTPRequest.run("/sales/most-sold-days")


class SoldDaysForBookListAPIView(BaseSalesAPIView, ListAPIView):
    serializer_class = SoldDaysSerializer

    def get_queryset(self):
        book_id = self.kwargs["book_id"]
        return HTTPRequest.run("/sales/book/sold-days", book_id=book_id)
