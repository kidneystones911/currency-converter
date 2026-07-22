import requests
import json

base_currency = "USD"
target_currency = "BDT"

def get_exchange_rate():
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    print("Exchange rate fetched!")

def save_rates(data):
    with open("exchange_rates.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Rates saved!")

if __name__ == "__main__":
    get_exchange_rate()