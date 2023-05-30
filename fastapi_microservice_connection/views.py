from typing import Optional, Tuple
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from fastapi_microservice_connection.serializers import (
    SalesSchemaDisplaySerializer,
    MostSoldBookSerializer,
    MostSoldDaysSerializer,
    SoldDaysSerializer,
)
from fastapi_microservice_connection.servises import HTTPRequest
from utils.microsevice_url import URL


class BaseSalesAPIView(APIView):
    MICROSERVICE_URL: URL
    serializer_class: serializers.Serializer
    pagination_class = None

    query_params_fields: Optional[Tuple[str]] = None
    path_params_fields: Optional[Tuple[str]] = None

    def get_params(self, request, **kwargs):
        path_params = {}

        if self.path_params_fields:
            for field in self.path_params_fields:
                if field in kwargs:
                    path_params[field] = kwargs[field]

        query_params = {}

        if self.query_params_fields:
            for field in self.query_params_fields:
                if field in request.GET:
                    query_params[field] = request.GET[field]

        return path_params, query_params

    def get(self, request, *args, **kwargs):
        path_params, query_params = self.get_params(request, **kwargs)
        response_data = HTTPRequest().run(
            url=self.MICROSERVICE_URL,
            path_params=path_params,
            query_params=query_params,
        )

        serializer = self.serializer_class(data=response_data, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class AllSalesListAPIView(BaseSalesAPIView):
    serializer_class = SalesSchemaDisplaySerializer
    MICROSERVICE_URL = URL.ALL_SALES.value


class MostExpensiveSaleAPIView(BaseSalesAPIView):
    serializer_class = SalesSchemaDisplaySerializer
    MICROSERVICE_URL = URL.MOST_EXPENSIVE_SALE.value


class MostSoldBookByQuantityAPIView(BaseSalesAPIView):
    serializer_class = MostSoldBookSerializer
    MICROSERVICE_URL = URL.MOST_SOLD_BOOK_BY_QUANTITY.value


class MostSoldBookByPriceAPIView(BaseSalesAPIView):
    serializer_class = MostSoldBookSerializer
    MICROSERVICE_URL = URL.MOST_SOLD_BOOK_BY_PRICE.value


#
class SalesByUserListAPIView(BaseSalesAPIView):
    serializer_class = SalesSchemaDisplaySerializer
    path_params_fields = ("user_id",)
    MICROSERVICE_URL = URL.SALES_BY_USER.value


#
class SalesByDateListAPIView(BaseSalesAPIView):
    serializer_class = SalesSchemaDisplaySerializer
    query_params_fields = ("day",)
    MICROSERVICE_URL = URL.SALES_BY_DATE.value


class MostSoldDaysListAPIView(BaseSalesAPIView):
    serializer_class = MostSoldDaysSerializer
    MICROSERVICE_URL = URL.MOST_SOLD_DAYS.value


class SoldDaysForBookListAPIView(BaseSalesAPIView):
    serializer_class = SoldDaysSerializer
    path_params_fields = ("book_id",)
    MICROSERVICE_URL = URL.BOOK_SOLD_BY_DAY.value
