from datetime import date

import factory
from book.models import Author, Publisher, Book


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker("name")
    bio = factory.Faker("text")
    date_of_birth = factory.Faker("date_of_birth", minimum_age=18, maximum_age=90)
    date_of_death = factory.Faker(
        "date_between", start_date=date(1950, 1, 1), end_date=date(2020, 12, 31)
    )


class PublisherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Publisher

    name = factory.Faker("company")
    description = factory.Faker("text")


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker("sentence", nb_words=4)
    author = factory.SubFactory(AuthorFactory)
    publisher = factory.SubFactory(PublisherFactory)
    description = factory.Faker("text")
    price = factory.Faker("pydecimal", min_value=1, max_value=1000, right_digits=2)
    genre = factory.Faker("word")
    publication_date = factory.Faker("date_this_decade")
    cover_image = factory.django.ImageField(color="blue")
    language = factory.Faker("language_code")
    available_stock = factory.Faker("pyint", min_value=0, max_value=1000)
    rating = factory.Faker("pyfloat", left_digits=1, right_digits=1, positive=True)
