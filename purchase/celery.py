import requests
from celery import Celery, shared_task

# Create a Celery instance
from rest_framework import status

app = Celery('celery', broker='pyamqp://guest@localhost//')


app.autodiscover_tasks()


@shared_task
def send_purchase_data_to_api(purchase_data):
    response = requests.post("http://127.0.0.1:8001/api", json=purchase_data)
    if response.status_code == status.HTTP_200_OK:
        print("POST request successful")
    else:
        print(f"POST request failed with status code: {response.status_code}")
