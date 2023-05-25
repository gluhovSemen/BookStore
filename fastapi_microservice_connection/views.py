from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

from fastapi_microservice_connection.serializers import SalesSchemaDisplaySerializer, MostSoldBookSerializer, \
    MostSoldDaysSerializer
from fastapi_microservice_connection.servises import HTTPRequest
from utils.permissions import IsOwner




class AllSalesListAPIView(ListAPIView):
    pagination_class = None
    serializer_class = SalesSchemaDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return HTTPRequest.run('/sales')


class MostExpensiveSaleAPIView(RetrieveAPIView):
    pagination_class = None
    serializer_class = SalesSchemaDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return HTTPRequest.run('/sales/most-expensive')
#
#
class MostSoldBookByQuantityAPIView(RetrieveAPIView):
    pagination_class = None
    serializer_class = MostSoldBookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return HTTPRequest.run('/sales/most-sold-book-by-quantity')

#
class MostSoldBookByPriceAPIView(RetrieveAPIView):
    pagination_class = None
    serializer_class = MostSoldBookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return HTTPRequest.run('/sales/most-sold-book-by-price')

#
# class SalesByUserListAPIView(ListAPIView):
#     pagination_class = None
#     serializer_class = SalesSchemaDisplaySerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         user_id = self.kwargs['user_id']
#         return get_sales_by_user(user_id)
#
#
# class SalesByDateListAPIView(ListAPIView):
#     pagination_class = None
#     serializer_class = SalesSchemaDisplaySerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         day = self.request.query_params.get('day')
#         return get_sales_by_day(day)
#
#
class MostSoldDaysListAPIView(ListAPIView):
    pagination_class = None
    serializer_class = MostSoldDaysSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return HTTPRequest.run('/sales/most-sold-days')

#
# class SoldDaysForBookListAPIView(ListAPIView):
#     pagination_class = None
#     serializer_class = str
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         book_id = self.kwargs['book_id']
#         return get_sold_days_for_book(book_id)