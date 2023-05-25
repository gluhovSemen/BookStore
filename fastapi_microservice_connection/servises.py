from abc import abstractmethod, ABC

import requests


class SalesAPI(ABC):
    base_url = "http://127.0.0.1:8001/api"  # Replace with your base URL

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
    def __init__(self, user_id, url="/sales/user/"):
        self.user_id = user_id
        self.url = url + str(user_id)

    def get_url(self):
        return f"{self.base_url}{self.url}"


class GetSalesByDay(SalesAPI):
    def __init__(self, day, url="/sales/date"):
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
    def __init__(self, book_id, url="/sales/book/"):
        self.book_id = book_id
        self.url = url + str(book_id) + "/sold-days"

    def get_url(self):
        return f"{self.base_url}{self.url}"


class HTTPRequest:
    MAPPER = {
        "/sales": GetAllSales,
        "/sales/most-expensive": GetMostExpensiveSale,
        "/sales/most-sold-book-by-quantity": GetMostSoldBookByQuantity,
        "/sales/most-sold-book-by-price": GetMostSoldBookByPrice,
        "/sales/most-sold-days": GetMostSoldDays,
    }

    @classmethod
    def run(cls, dynamic_value: str, **kwargs):
        if dynamic_value in cls.MAPPER:
            request_class = cls.MAPPER[dynamic_value]
            request_obj = request_class(dynamic_value)
            return request_obj.make_request()
