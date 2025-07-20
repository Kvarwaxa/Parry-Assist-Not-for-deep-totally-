from capture import start_capture
from detector import DetectionEngine
from overlay import OverlayManager
import threading, time, json, os

CONFIG_PATH = 'config.json'
DEFAULT_CONFIG = {
    "detection_threshold": 0.75,
    "scan_interval_min_ms": 90,
    "scan_interval_max_ms": 130,
    "capture_region": "fullscreen"
}

if not os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(DEFAULT_CONFIG, f)

with open(CONFIG_PATH) as f:
    config = json.load(f)

if not os.path.exists("templates"):
    os.makedirs("templates")

detector = DetectionEngine(config)
overlay = OverlayManager()

def detection_loop():
    while True:
        frame = start_capture(config)
        if detector.detect(frame):
            overlay.trigger()
        time.sleep(detector.get_scan_delay())

threading.Thread(target=detection_loop, daemon=True).start()
overlay.run()
