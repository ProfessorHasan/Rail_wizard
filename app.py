import requests

url = "https://railspaapi.shohoz.com/v1.0/web/train-routes"
payload = {
    "model": "DHAKA_CHITTAGONG_MAILEXP",  # Use actual train model name
    "departure_date_time": "2025-05-27"
}
headers = {"Content-Type": "application/json"}

res = requests.post(url, json=payload, headers=headers)
print(res.json())
