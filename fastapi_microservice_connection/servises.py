import requests

base_url = "http://127.0.0.1:8001/api"


# def create_sale(sale_data):
#     url = f"{base_url}/"
#     response = requests.post(url, json=sale_data)
#     if response.status_code == 201:
#         new_sale = response.json()
#         return new_sale
#     else:
#         return None


def get_all_sales():
    url = f"{base_url}/sales"
    response = requests.get(url)
    if response.status_code == 200:
        all_sales = response.json()
        return all_sales
    else:
        return None


def get_most_expensive_sale():
    url = f"{base_url}/sales/most-expensive"
    response = requests.get(url)
    if response.status_code == 200:
        most_expensive_sale = response.json()
        return most_expensive_sale
    else:
        return None


def get_most_sold_book_by_quantity():
    url = f"{base_url}/sales/most-sold-book-by-quantity"
    response = requests.get(url)
    if response.status_code == 200:
        most_sold_book_by_quantity = response.json()
        return most_sold_book_by_quantity
    else:
        return None


def get_most_sold_book_by_price():
    url = f"{base_url}/sales/most-sold-book-by-price"
    response = requests.get(url)
    if response.status_code == 200:
        most_sold_book_by_price = response.json()
        return most_sold_book_by_price
    else:
        return None


def get_sales_by_user(user_id):
    url = f"{base_url}/sales/user/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        sales_by_user = response.json()
        return sales_by_user
    else:
        return None


def get_sales_by_day(day):
    url = f"{base_url}/sales/date"
    params = {"day": day}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        sales_by_day = response.json()
        return sales_by_day
    else:
        return None


def get_most_sold_days():
    url = f"{base_url}/sales/most-sold-days"
    response = requests.get(url)
    if response.status_code == 200:
        most_sold_days = response.json()
        return most_sold_days
    else:
        return None


def get_sold_days_for_book(book_id):
    url = f"{base_url}/sales/book/{book_id}/sold-days"
    response = requests.get(url)
    if response.status_code == 200:
        sold_days_for_book = response.json()
        return sold_days_for_book
    else:
        return None
