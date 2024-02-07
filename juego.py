from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

# Definir los tipos de bloques para simplificar el entorno
block_types = ['grass', 'water']  # 'water' para el mar alrededor
current_block = 0  # Índice para el bloque actual, comenzando con 'grass'

class Voxel(Button):
    def __init__(self, position=(0,0,0), block_type='grass'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=block_type,
            color=color.white if block_type == 'grass' else color.blue,
            highlight_color=color.lime,
        )
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                # Añadir un nuevo bloque en la posición apuntada
                Voxel(position=self.position + mouse.normal, block_type=block_types[current_block])
            elif key == 'right mouse down':
                # Destruir el bloque seleccionado
                destroy(self)

def generate_terrain(chunk_size=20, water_level=-1):
    # Crear un terreno con una elevación más uniforme
    for z in range(-chunk_size, chunk_size + 1):
        for x in range(-chunk_size, chunk_size + 1):
            # Generar principalmente bloques 'grass'
            Voxel(position=(x, water_level, z), block_type='grass')
    
    # Crear "mar" alrededor del terreno
    for z in range(-chunk_size-5, chunk_size+6):
        for x in range(-chunk_size-5, chunk_size+6):
            if x <= -chunk_size or x >= chunk_size or z <= -chunk_size or z >= chunk_size:
                Voxel(position=(x, water_level-1, z), block_type='water')

generate_terrain()  # Llamar a la función con los parámetros por defecto para generar el terreno

player = FirstPersonController()
Sky()  # Agregar un cielo para completar el ambiente

app.run()  # Iniciar la aplicación
