import os
from abc import abstractmethod, ABC
import requests
from dotenv import load_dotenv

load_dotenv()


class SalesAPI(ABC):
    base_url = os.getenv("URL")

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
    def __init__(self, url):
        self.url = url

    def get_url(self):
        return f"{self.base_url}{self.url}"


class GetMostExpensiveSale(SalesAPI):
    def __init__(self, url):
        self.url = url

    def get_url(self):
        return f"{self.base_url}{self.url}"


class GetMostSoldBookByQuantity(SalesAPI):
    def __init__(self, url):
        self.url = url

    def get_url(self):
        return f"{self.base_url}{self.url}"


class GetMostSoldBookByPrice(SalesAPI):
    def __init__(self, url):
        self.url = url

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
    def __init__(self, url):
        self.url = url

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
        "/sales": GetAllSales,
        "/sales/most-expensive": GetMostExpensiveSale,
        "/sales/most-sold-book-by-quantity": GetMostSoldBookByQuantity,
        "/sales/most-sold-book-by-price": GetMostSoldBookByPrice,
        "/sales/most-sold-days": GetMostSoldDays,
        "/sales/user": GetSalesByUser,
        "/sales/date": GetSalesByDay,
        "/sales/book/sold-days": GetSoldDaysForBook,
    }

    @classmethod
    def run(cls, url: str, **kwargs):
        if url in cls.MAPPER:
            request_class = cls.MAPPER[url]
            request_obj = request_class(url=url, **kwargs)
            return request_obj.make_request()
