import requests


def send_purchase_data_to_api(purchase_data):
    try:
        response = requests.post("http://127.0.0.1:8001/api", json=purchase_data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
