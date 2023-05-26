import requests
from celery import Celery, shared_task

# Create a Celery instance
from rest_framework import status

app = Celery("celery", broker="pyamqp://guest@localhost//")

app.autodiscover_tasks()


def send_purchase_data_to_api(purchase_data):
    try:
        response = requests.post("http://127.0.0.1:8001/api", json=purchase_data)
        response.raise_for_status()  # Check if the request was successful
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
