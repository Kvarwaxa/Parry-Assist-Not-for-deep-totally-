import mss, numpy as np, cv2

def start_capture(config):
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        img = sct.grab(monitor)
        frame = np.array(img)
        return cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
