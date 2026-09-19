import psutil
import time

while True:
    cpu_usage = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory()
    ram_used = ram.used / (1024 ** 3)
    ram_total = ram.total / (1024 ** 3)

    print("PC MONITOR")
    print("--------------------")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"RAM: {ram_used:.1f} GB / {ram_total:.1f} GB")
    print("--------------------")

    time.sleep(1)