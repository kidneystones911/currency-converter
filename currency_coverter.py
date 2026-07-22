import requests

def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    print("Exchange rate fetched!")

if __name__ == "__main__":
    get_exchange_rate()