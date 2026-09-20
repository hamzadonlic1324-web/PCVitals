# PCVitals

PCVitals is a lightweight Windows hardware monitoring overlay built with Python.

It shows live system stats in a small horizontal bar at the bottom-left of your screen.

## Features

- CPU usage
- RAM usage
- NVIDIA GPU usage
- GPU temperature
- VRAM usage
- Always-on-top desktop overlay
- Updates every second
- Windows system tray icon
- Show or hide the overlay from the tray
- Exit PCVitals from the tray
- Standalone Windows executable support

## Current GPU Support

PCVitals currently uses NVIDIA NVML, so GPU monitoring is built for NVIDIA graphics cards.

## Run From Python

1. Install Python 3.
2. Clone this repository.
3. Install the required packages:

```bash
py -m pip install -r requirements.txt
```

4. Run PCVitals:

```bash
py main.py
```

Right-click the PCVitals system tray icon to show the overlay, hide it, or exit the app.

Press Escape while the overlay is focused to close PCVitals.

## Build a Windows EXE

Install PyInstaller:

```bash
py -m pip install pyinstaller
```

Build the executable:

```bash
pyinstaller --onefile --windowed --name PCVitals main.py
```

The finished executable will be inside the `dist` folder.

## Version

Current development version: v1.1.0

v1.1.0 adds a Windows system tray icon with Show Overlay, Hide Overlay, and Exit PCVitals controls.

## Built With

- Python
- Tkinter
- psutil
- NVIDIA NVML through nvidia-ml-py
- pystray
- Pillow

## Author

Created by Hamza.
