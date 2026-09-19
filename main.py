import psutil
import time
import pynvml

pynvml.nvmlInit()
gpu = pynvml.nvmlDeviceGetHandleByIndex(0)

while True:
    cpu_usage = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory()
    ram_used = ram.used / (1024 ** 3)
    ram_total = ram.total / (1024 ** 3)

    gpu_name = pynvml.nvmlDeviceGetName(gpu)
    gpu_usage = pynvml.nvmlDeviceGetUtilizationRates(gpu).gpu
    gpu_temp = pynvml.nvmlDeviceGetTemperature(
        gpu,
        pynvml.NVML_TEMPERATURE_GPU
    )

    vram = pynvml.nvmlDeviceGetMemoryInfo(gpu)
    vram_used = vram.used / (1024 ** 3)
    vram_total = vram.total / (1024 ** 3)

    print("PC VITALS")
    print("-------------------------")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"RAM: {ram_used:.1f} GB / {ram_total:.1f} GB")
    print()
    print(f"GPU: {gpu_name}")
    print(f"GPU Usage: {gpu_usage}%")
    print(f"GPU Temperature: {gpu_temp}°C")
    print(f"VRAM: {vram_used:.1f} GB / {vram_total:.1f} GB")
    print("-------------------------")

    time.sleep(1)