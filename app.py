import requests

url = "https://railspaapi.shohoz.com/v1.0/web/train-routes"
payload = {
    "model": "DHAKA_CHITTAGONG_MAILEXP",  # Make sure this is a valid train model
    "departure_date_time": "2025-05-27"
}
headers = {"Content-Type": "application/json"}

res = requests.post(url, json=payload, headers=headers)

print("Status Code:", res.status_code)
print("Response Text:", res.text)  # Print raw text before trying to parse JSON

# Only try to parse JSON if status is OK and response is not empty
if res.ok and res.text.strip():
    try:
        print("Response JSON:", res.json())
    except Exception as e:
        print("JSON decoding failed:", e)
else:
    print("API call failed or returned no content.")
