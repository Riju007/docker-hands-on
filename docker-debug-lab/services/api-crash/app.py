import time
print("Starting crash service")
time.sleep(3)

raise Exception("Simulated production crash")
