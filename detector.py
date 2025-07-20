import cv2, os, numpy as np, random

class DetectionEngine:
    def __init__(self, config):
        self.threshold = config["detection_threshold"]
        self.templates = []
        self.load_templates()
        self.min_delay = config["scan_interval_min_ms"] / 1000.0
        self.max_delay = config["scan_interval_max_ms"] / 1000.0

    def load_templates(self):
        for file in os.listdir("templates"):
            if file.endswith(".png"):
                img = cv2.imread(os.path.join("templates", file), 0)
                self.templates.append(img)

    def detect(self, frame):
        for template in self.templates:
            res = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(res)
            if max_val >= self.threshold:
                return True
        return False

    def get_scan_delay(self):
        return random.uniform(self.min_delay, self.max_delay)
