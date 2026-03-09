import requests
import time

while True:
    try:
        r = requests.get("http://db:9999")
        print(r.text)
    except Exception as e:
        print(f"Network Error: {e}")

    time.sleep(3)
