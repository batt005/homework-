import cv2
import numpy as np
import pyautogui
from ultralytics import YOLO
import time

model = YOLO("runs/detect/chill_guy_detector-2/weights/best.pt")

print("ИИ-кликер запущен!")
print("БЫСТРО открой вкладку браузера с игрой Chill Guy Clicker...")
time.sleep(5)

try:
    while True:

        screen = pyautogui.screenshot()
        frame = np.array(screen)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    
        results = model(frame, stream=True, verbose=False)

        for result in results:
            for box in result.boxes:
            
                if box.conf > 0.5: 
                   
                    x1, y1, x2, y2 = box.xyxy.tolist()[0]
                    center_x = int((x1 + x2) / 2)
                    center_y = int((y1 + y2) / 2)

                
                    pyautogui.click(center_x, center_y)
                    print(f"Клик по Chill Guy! Координаты: {center_x}, {center_y}")
                    
                    
                    time.sleep(0.05)
                    
except KeyboardInterrupt:
    print("ИИ-автокликер успешно остановлен.")
