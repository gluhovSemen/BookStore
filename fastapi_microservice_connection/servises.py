import enum
import os
from abc import abstractmethod, ABC
import requests
from dotenv import load_dotenv

from utils.MICROSERVICE_URL import URL

load_dotenv()


class SalesAPI(ABC):
    base_url = os.getenv("URL")

    def __init__(self, url):
        self.url = url

    @abstractmethod
    def get_url(self):
        pass

    def make_request(self, params=None):
        url = self.get_url()
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None


class GetAllSales(SalesAPI):

    def get_url(self):
        return f"{self.base_url}{self.url}"


class GetMostExpensiveSale(SalesAPI):

    def get_url(self):
        return f"{self.base_url}{self.url}"


class GetMostSoldBookByQuantity(SalesAPI):

    def get_url(self):
        return f"{self.base_url}{self.url}"


class GetMostSoldBookByPrice(SalesAPI):

    def get_url(self):
        return f"{self.base_url}{self.url}"


class GetSalesByUser(SalesAPI):
    def __init__(self, url, user_id):
        self.user_id = user_id
        self.url = url + "/" + str(self.user_id)

    def get_url(self):
        return f"{self.base_url}{self.url}"


class GetSalesByDay(SalesAPI):
    def __init__(self, url, day):
        self.day = day
        self.url = url

    def get_url(self):
        return f"{self.base_url}{self.url}"

    def make_request(self):
        params = {"day": self.day}
        return super().make_request(params)


class GetMostSoldDays(SalesAPI):
    def get_url(self):
        return f"{self.base_url}{self.url}"


class GetSoldDaysForBook(SalesAPI):
    def __init__(self, url, book_id):
        self.book_id = book_id
        self.url = url + "/" + str(book_id)

    def get_url(self):
        return f"{self.base_url}{self.url}"


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
        if url in cls.MAPPER:
            request_class = cls.MAPPER[url]
            request_obj = request_class(url=url, **kwargs)
            return request_obj.make_request()
