import cv2
import numpy as np
import logging
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import cv2
import numpy as np
import io
import time

class ARGame:
    def __init__(self):
            print ('inicio de clase ARgame')
    def capture_camera():
        cap = cv2.VideoCapture(0)  # Abre la cámara
        while True:
            ret, frame = cap.read()  # Lee un fotograma desde la cámara
            if not ret:
                break
            # Convierte el fotograma a bytes
            _, img_encoded = cv2.imencode(".jpg", frame)
            # Convierte los bytes a un objeto io.BytesIO
            img_bytes = io.BytesIO(img_encoded.tobytes())
            # Devuelve el fotograma como una respuesta de transmisión
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + img_bytes.read() + b'\r\n')
            time.sleep(0.1)
        cap.release()
