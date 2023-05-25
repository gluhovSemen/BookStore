from django.urls import path
from fastapi_microservice_connection.views import (
    # CreateSale,
    AllSalesListAPIView,
    MostExpensiveSaleAPIView,
    MostSoldBookByQuantityAPIView,
    MostSoldBookByPriceAPIView,
    SalesByUserListAPIView,
    SalesByDateListAPIView,
    MostSoldDaysListAPIView,
    SoldDaysForBookListAPIView,
)

urlpatterns = [
    path("sales", AllSalesListAPIView.as_view(), name="all-sales"),
    path("sales/most-expensive", MostExpensiveSaleAPIView.as_view(), name="most-expensive-sale"),
    path("sales/most-sold-book-by-quantity", MostSoldBookByQuantityAPIView.as_view(), name="most-sold-book-by-quantity"),
    path("sales/most-sold-book-by-price", MostSoldBookByPriceAPIView.as_view(), name="most-sold-book-by-price"),
    path("sales/user/<int:user_id>", SalesByUserListAPIView.as_view(), name="sales-by-user"),
    path("sales/date", SalesByDateListAPIView.as_view(), name="sales-by-date"),
    path("sales/most-sold-days", MostSoldDaysListAPIView.as_view(), name="most-sold-days"),
    path("sales/book/<int:book_id>/sold-days", SoldDaysForBookListAPIView.as_view(), name="sold-days-for-book"),
    # path("create-sale", CreateSale.as_view(), name="create-sale"),
]
