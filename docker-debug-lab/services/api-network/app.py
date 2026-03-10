import requests
import time

while True:
    try:
        r = requests.get("http://db:9999")
        print(r.text)
        print("Trying to reach service: db:9999")
    except Exception as e:
        print(f"Network Error: {e}")

    time.sleep(3)
