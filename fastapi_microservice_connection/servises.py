import enum
import os
import requests
from dotenv import load_dotenv

from utils.microsevice_url import URL

load_dotenv()


class SalesAPI:
    BASE_URL = os.getenv("URL")

    @staticmethod
    def url_parce(url, **kwargs):
        url = SalesAPI.BASE_URL + url
        path_params = kwargs.get("path_params", {})
        query_params = kwargs.get("query_params", {})
        if path_params:
            url += "/" + str(sum(path_params.values()))
        if query_params:
            url += "?day=" + query_params["day"]
        return url

    @classmethod
    def run(cls, url, **kwargs):
        url_full = cls.url_parce(url, **kwargs)
        response = requests.get(url_full)
        return response.json()


class GetAllSales(SalesAPI):
    pass


class GetMostExpensiveSale(SalesAPI):
    pass


class GetMostSoldBookByQuantity(SalesAPI):
    pass


class GetMostSoldBookByPrice(SalesAPI):
    pass


class GetSalesByUser(SalesAPI):
    pass


class GetSalesByDay(SalesAPI):
    pass


class GetMostSoldDays(SalesAPI):
    pass


class GetSoldDaysForBook(SalesAPI):
    pass


class HTTPRequest:
    MAPPER = {
        URL.ALL_SALES.value: GetAllSales,
        URL.MOST_EXPENSIVE_SALE.value: GetMostExpensiveSale,
        URL.MOST_SOLD_BOOK_BY_QUANTITY.value: GetMostSoldBookByQuantity,
        URL.MOST_SOLD_BOOK_BY_PRICE.value: GetMostSoldBookByPrice,
        URL.MOST_SOLD_DAYS.value: GetMostSoldDays,
        URL.SALES_BY_USER.value: GetSalesByUser,
        URL.SALES_BY_DATE.value: GetSalesByDay,
        URL.BOOK_SOLD_BY_DAY.value: GetSoldDaysForBook,
    }

    @classmethod
    def run(cls, url: enum, **kwargs):
        return cls.MAPPER[url]().run(url=url, **kwargs)
