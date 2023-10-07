# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dugonzal <dugonzal@student.42urduliz.com>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/07 12:19:03 by Dugonzal          #+#    #+#              #
#    Updated: 2023/10/07 12:23:02 by Dugonzal         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from fastapi import FastAPI, WebSocket
#from ar_logic import CameraLogic

app = FastAPI()

# Rutas y funciones para la API
"""
@app.websocket("/camera")
async def camera_endpoint(websocket: WebSocket):
    await websocket.accept()
    camera = CameraLogic()  # Crea una instancia de la lógica de la cámara desde ar_logic
    while True:
        frame = camera.capture_frame()  # Llama a una función en ar_logic para capturar el cuadro
        await websocket.send_bytes(frame)

# Otras rutas y funciones que puedas necesitar para tu aplicación FastAPI
"""
@app.get("/")
async def read_root():
    return {"message": "Welcome to the AR Game API!"}

@app.get("/info")
async def get_info():
    return {"info": "This is an API for the AR Game."}

# Agrega más rutas y funciones según las necesidades específicas de tu aplicación

