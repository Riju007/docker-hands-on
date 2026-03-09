import time

data = []

while True:
    data.append("x" * 1000000)
    print(f"Allocated chunks: {len(data)}")
    time.sleep(1)
