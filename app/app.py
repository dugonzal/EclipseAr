# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dugonzal <dugonzal@student.42urduliz.com>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/07 12:19:03 by Dugonzal          #+#    #+#              #
#    Updated: 2023/10/08 12:24:48 by Dugonzal         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from fastapi import FastAPI, WebSocket
from logic.logic import ARGame  # Importa la clase ARGameR
import logging
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


from fastapi.responses import StreamingResponse
import cv2
import numpy as np
import io
import time

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Configura el manejo de archivos estáticos (CSS, JavaScript, etc.)
app.mount("/static", StaticFiles(directory="./static"), name="static")

# Configura el motor de plantillas Jinja2
templates = Jinja2Templates(directory="./templates")

# Lista de nombres de usuario (simulación de datos)
users = ["Alice", "Bob", "Charlie", "David"]

@app.get("/")
async def read_root(request: Request):
    # Renderiza la página HTML con la lista de usuarios
    return templates.TemplateResponse("main.html", {"request": request, "users": users})

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
