# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dugonzal <dugonzal@student.42urduliz.com>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/07 12:19:03 by Dugonzal          #+#    #+#              #
#    Updated: 2023/10/07 13:30:02 by Dugonzal         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from fastapi import FastAPI, WebSocket
from logic.logic import ARGame  # Importa la clase ARGameR
import logging

from fastapi.responses import StreamingResponse
import cv2
import numpy as np
import io
import time



logging.basicConfig(level=logging.DEBUG)
app = FastAPI()


# Función para capturar la cámara en tiempo real
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
        # Agrega un pequeño retraso para ajustar la velocidad de transmisión
        time.sleep(0.1)

    cap.release()

@app.get("/cam")
async def video_feed():
    return StreamingResponse(capture_camera(), media_type="multipart/x-mixed-replace;boundary=frame")

# Rutas y funciones para la API
@app.get("/")
async def read_root():
    return {"message": "Welcome to the AR Game API!"}

@app.get("/info")
async def get_info():
    return {"info": "This is an API for the AR Game."}

# Agrega más rutas y funciones según las necesidades específicas de tu aplicación

