import enum


class URL(enum.Enum):
    ALL_SALES = "/sales"
    MOST_EXPENSIVE_SALE = "/sales/most-expensive"
    MOST_SOLD_BOOK_BY_QUANTITY = "/sales/most-sold-book-by-quantity"
    MOST_SOLD_BOOK_BY_PRICE = "/sales/most-sold-book-by-price"
    MOST_SOLD_DAYS = "/sales/most-sold-days"
    SALES_BY_USER = "/sales/user"
    SALES_BY_DATE = "/sales/date"
    BOOK_SOLD_BY_DAY = "/sales/book/sold-days"
