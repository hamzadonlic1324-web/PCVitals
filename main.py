import tkinter as tk
import threading

import psutil
import pynvml
import pystray
from PIL import Image, ImageDraw


# Hardware setup
pynvml.nvmlInit()
gpu = pynvml.nvmlDeviceGetHandleByIndex(0)


# Overlay setup
root = tk.Tk()
root.title("PCVitals")
root.geometry("700x45")
root.configure(bg="#111111")
root.overrideredirect(True)
root.attributes("-topmost", True)
root.attributes("-alpha", 0.85)

label = tk.Label(
    root,
    text="Starting PCVitals...",
    font=("Consolas", 11),
    fg="white",
    bg="#111111"
)
label.pack(padx=12, pady=10)

root.update_idletasks()

screen_height = root.winfo_screenheight()
window_height = 45
root.geometry(f"700x45+10+{screen_height - window_height - 50}")

psutil.cpu_percent(interval=None)


def update_vitals():
    if not root.winfo_exists():
        return

    cpu_usage = psutil.cpu_percent(interval=None)

    ram = psutil.virtual_memory()
    ram_used = ram.used / (1024 ** 3)
    ram_total = ram.total / (1024 ** 3)

    gpu_usage = pynvml.nvmlDeviceGetUtilizationRates(gpu).gpu
    gpu_temp = pynvml.nvmlDeviceGetTemperature(
        gpu,
        pynvml.NVML_TEMPERATURE_GPU
    )

    vram = pynvml.nvmlDeviceGetMemoryInfo(gpu)
    vram_used = vram.used / (1024 ** 3)
    vram_total = vram.total / (1024 ** 3)

    text = (
        f"CPU {cpu_usage:.0f}%   |   "
        f"RAM {ram_used:.1f}/{ram_total:.1f} GB   |   "
        f"GPU {gpu_usage}%   |   "
        f"GPU TEMP {gpu_temp}°C   |   "
        f"VRAM {vram_used:.1f}/{vram_total:.1f} GB"
    )

    label.config(text=text)
    root.after(1000, update_vitals)


def create_tray_image():
    image = Image.new("RGB", (64, 64), "#111111")
    draw = ImageDraw.Draw(image)

    draw.rounded_rectangle(
        (6, 6, 58, 58),
        radius=10,
        outline="white",
        width=4
    )

    draw.text(
        (20, 22),
        "PC",
        fill="white"
    )

    return image


def show_overlay(icon=None, item=None):
    root.after(0, root.deiconify)


def hide_overlay(icon=None, item=None):
    root.after(0, root.withdraw)


def exit_pcvitals(icon=None, item=None):
    if icon is not None:
        icon.stop()

    root.after(0, root.destroy)


tray_icon = pystray.Icon(
    "PCVitals",
    create_tray_image(),
    "PCVitals",
    menu=pystray.Menu(
        pystray.MenuItem("Show Overlay", show_overlay),
        pystray.MenuItem("Hide Overlay", hide_overlay),
        pystray.MenuItem("Exit PCVitals", exit_pcvitals)
    )
)

tray_thread = threading.Thread(
    target=tray_icon.run,
    daemon=True
)
tray_thread.start()

root.bind("<Escape>", lambda event: exit_pcvitals(tray_icon))

update_vitals()
root.mainloop()

tray_icon.stop()
pynvml.nvmlShutdown()
