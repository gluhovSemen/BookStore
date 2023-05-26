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
from utils.MICROSERVICE_URL import URL


class BaseSalesAPIView(APIView):
    pagination_class = None
    serializer_class = SalesSchemaDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]

    def run_http_request(self, url, **kwargs):
        return HTTPRequest.run(url, **kwargs)


class AllSalesListAPIView(BaseSalesAPIView, ListAPIView):
    queryset = BaseSalesAPIView().run_http_request(URL.ALL_SALES.value)


class MostExpensiveSaleAPIView(BaseSalesAPIView, RetrieveAPIView):
    queryset = BaseSalesAPIView().run_http_request(URL.MOST_EXPENSIVE_SALE.value)


class MostSoldBookByQuantityAPIView(BaseSalesAPIView, RetrieveAPIView):
    serializer_class = MostSoldBookSerializer
    queryset = BaseSalesAPIView().run_http_request(URL.MOST_SOLD_BOOK_BY_QUANTITY.value)


class MostSoldBookByPriceAPIView(BaseSalesAPIView, RetrieveAPIView):
    serializer_class = MostSoldBookSerializer
    queryset = BaseSalesAPIView().run_http_request(URL.MOST_SOLD_BOOK_BY_PRICE.value)


class SalesByUserListAPIView(BaseSalesAPIView, ListAPIView):
    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return BaseSalesAPIView().run_http_request(URL.SALES_BY_USER.value, user_id=user_id)


class SalesByDateListAPIView(BaseSalesAPIView, ListAPIView):
    # @swagger_auto_schema(manual_parameters=[
    #     openapi.Parameter('day', openapi.IN_QUERY, description='The day to filter sales by', type=openapi.TYPE_STRING),
    # ])
    def get_queryset(self):
        day = self.request.query_params.get("day")
        return BaseSalesAPIView().run_http_request(URL.SALES_BY_DATE.value, day=day)


class MostSoldDaysListAPIView(BaseSalesAPIView, ListAPIView):
    serializer_class = MostSoldDaysSerializer
    queryset = BaseSalesAPIView().run_http_request(URL.MOST_SOLD_DAYS.value)


class SoldDaysForBookListAPIView(BaseSalesAPIView, ListAPIView):
    serializer_class = SoldDaysSerializer

    def get_queryset(self):
        book_id = self.kwargs["book_id"]
        return BaseSalesAPIView().run_http_request(URL.BOOK_SOLD_BY_DAY.value, book_id=book_id)
